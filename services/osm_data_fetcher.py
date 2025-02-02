import overpass
import pandas as pd
from shapely import Polygon
from typing import Dict, List
from Levenshtein import distance as lev
import os


class OSMDataFetcher:
    _api = None

    def __init__(self) -> None:
        self._api = overpass.API()
    
    def get_substations_by_polygons(self, multi_polygon: Polygon):
        if multi_polygon.geom_type == 'Polygon':
            bounds = multi_polygon.bounds
            #vertices = [(round(coord[0], 6), round(coord[1], 6)) for coord in polygons.exterior.coords]
        if multi_polygon.geom_type == 'MultiPolygon':
            for polygon in multi_polygon:
                print('HEY BE CAREFUL! REMEMBER TO EXCLUDE THE SMALLER POLYGONS AND KEEP ONLY THE BIG ONE')
                # GEOPANDAS FUNCTION WITHIN
                bounds = multi_polygon.bounds
                #vertices = [(round(coord[0], 6), round(coord[1], 6)) for coord in polygon.exterior.coords]
        
        sw = (bounds[0], bounds[1])
        se = (bounds[2], bounds[1])
        ne = (bounds[2], bounds[3])
        nw = (bounds[0], bounds[3])

        rectangle_coordinates = f'"{sw[1]} {sw[0]} {se[1]} {se[0]} {ne[1]} {ne[0]} {nw[1]} {nw[0]} {sw[1]} {sw[0]}"'

        query = f"way[\"power\"=\"substation\"](poly: {rectangle_coordinates});out geom;"
        response = self._api.Get(query)

        return response

    def analyze_substations_tags_by_state(self, state: str):
        query = f"""
            area[name="{state}"]->.searchArea;
            (
                way["power"="substation"](area.searchArea);
            );
            out geom;
        """
        response = self._api.Get(query)

        features_with_coords = [feature for feature in response.features if len(feature.geometry['coordinates']) > 0]

        number_of_substations_found = len(features_with_coords)
        properties = {
            property for feature in features_with_coords for property in feature.properties
        }

        property_summary_dict: Dict[str, int] = {}
        for property in properties:
            for feature in features_with_coords:
                if property in feature.properties:
                    property_summary_dict[property] = property_summary_dict.get(property, 0) + 1

        analysis_result_df = pd.DataFrame(property_summary_dict.items())
        analysis_result_df.columns = ['property name', 'number of occurences']
        analysis_result_df.to_excel(f'./output/{state}_substation_analysis.xlsx')

        return analysis_result_df


    def analyze_substations_tags_values_by_state(self, state: str, property_names: List[str]):
        query = f"""
            area[name="{state}"]->.searchArea;
            (
                way["power"="substation"](area.searchArea);
            );
            out geom;
        """
        response = self._api.Get(query)

        features_with_coords = [feature for feature in response.features if len(feature.geometry['coordinates']) > 0]
        values_dict: Dict[str, set] = {}
        for property in property_names:
            for feature in features_with_coords:
                property_value = next((
                    property_value for property_key, property_value in feature.properties.items() if property_key == property
                ), None)
                if property_value is not None:
                    if property not in values_dict:
                        values_dict[property] = set() 
                    values_dict[property].add(property_value)

        final_analysis_df = pd.DataFrame(values_dict.items())
        final_analysis_df.to_excel(f'./output/{state}_tags_values_analysis.xlsx')


    def analyze_substations_tags_values_by_state_distribution(self, state: str, property_names: List[str]):
        query = f"""
             area[name="{state}"]->.searchArea;
            (
                way["power"="substation"](area.searchArea);
            );
            out geom;
        """
        response = self._api.Get(query)

        features_with_coords = [feature for feature in response.features if len(feature.geometry['coordinates']) > 0]
        distribution_substations = []
        for feature in features_with_coords:
            if all(key not in feature.properties for key in ["disused", "disused:transformer", "abandoned", 'disused', 'historic', 'plant:source',
            'operational_status','ruins','demolished:building','building:disused','end_date']):
                for property in property_names:
                    if property in feature.properties and feature.properties[property] == "distribution":
                        distribution_substations.append(feature)

        print(len(distribution_substations))
            
        # Prepare data for CSV
        data_for_csv = []
        for substation in distribution_substations:
            coords = substation.geometry['coordinates']
            operator = substation.properties.get('operator', 'unknown')  # Get the operator, or 'N/A' if it doesn't exist
            data_for_csv.append([substation, coords[0], coords[1], operator])

        # Convert to DataFrame and save as CSV
        final_analysis_df = pd.DataFrame(data_for_csv, columns=['Substation', 'Longitude', 'Latitude', 'Operator'])
        final_analysis_df.to_csv(f'./output/{state}_distribution_substations.csv', index=False)


    def get_distinct_operators(self, csv_file):
        df = pd.read_csv(csv_file)
        distinct_operators = set(df['Operator'])

        return distinct_operators

    def filter_operators(self, csv_file, operators_to_exclude):
        df = pd.read_csv(csv_file)
        filtered_df = df[~df['Operator'].isin(operators_to_exclude)]
        # Get the filename from the csv_file path
        filename = os.path.basename(csv_file)
        filtered_df.to_csv(f'./output/filtered_{filename}', index=False)
        return filtered_df




    
    def compare_operators_with_names(self, distinct_operators, names):
        matching_operators = []
        for operator in distinct_operators: 
            for name in names:
                # tmp_operator = operator
                # tmp_name = name
                # if lev(operator, name) < 6:
                if isinstance(operator, str) and lev(operator, name) < 6:

                    matching_operators.append({operator: name})
        return matching_operators


names = [
    "AcegasApsAmga Spa",
    "e-distribuzione S.p.A.",
    "Assem SPA",
    "RetiPiù Srl",
    "V-RETI",
    "ASM Bressanone S.p.A.",
    "DISTRIBUZIONE ELETTRICA ADRIATICA SRL",
    "AMAIE SPA",
    "SECAB SOCIETÀ COOPERATIVA",
    "Unareti S.p.A.",
    "E.U.M. SOC. COOP. PER L'ENERGIA E L'AMBIENTE MOSO S.C.R.L.",
    "Terni Distribuzione Elettrica",
    "Società Cooperativa Elettrica di Distribuzione Campo Tures",
    "AZIENDA RETI ELETTRICHE SRL",
    "Azienda Intercomunale Rotaliana Spa - SB",
    "EDYNA SRL",
    "DEVAL",
    "ARETI SPA",
    "Dea Spa",
    "ASM Vercelli spa",
    "INRETE Distribuzione Energia S.p.A.",
    "SET DISTRIBUZIONE",
    "Ireti spa",
    "LD RETI S.R.L.",
    "AZIENDA SPECIALIZZATA SETTORE MULTISERVIZI S.P.A."
]


