import geopandas as gpd
from shapely.geometry import Polygon
import overpass
import pandas as pd

class SubstationFinder:
    def __init__(self, gpkg_file_path: str):
        self.gpkg_file_path = gpkg_file_path
        self.overpass_api = overpass.API()

    def get_border_polygon_by_id(self, border_id: int):
        # Load the GPKG file and extract the border geometry for the given ID
        gdf = gpd.read_file(self.gpkg_file_path, layer="primary_cabins")
        border_gdf = gdf[gdf['OBJECTID'] == border_id]

        if border_gdf.empty:
            raise ValueError(f"No border found with ID {border_id}")
        
        # Extract geometry of the border
        border_polygon = border_gdf.geometry.iloc[0]
        return border_polygon

    def get_substations_in_polygon(self, polygon: Polygon):
        bounds = polygon.bounds
        sw = (bounds[0], bounds[1])
        ne = (bounds[2], bounds[3])

        # Define the Overpass query for substations within the polygon bounds
        query = f"""
        [out:json];
        way["power"="substation"]
        (poly: "{sw[1]} {sw[0]} {ne[1]} {ne[0]}");
        out geom;
        """
        print("Generated Overpass query:", query)  # For debugging purposes
        response = self.overpass_api.Get(query)

        # Print the full response for debugging
        print("Overpass API response:", response)
        
        if len(response['elements']) == 0:
            raise ValueError("No substations found within the border polygon.")
        
        return response

    def filter_substations(self, response):
        # If more than one substation is found, apply filters (modify the criteria if needed)
        substations = response['elements']
        if len(substations) > 1:
            # Apply filtering logic here (e.g., operator, tag criteria, etc.)
            filtered_substations = [
                s for s in substations 
                if "distribution" in s.get('tags', {}).get('substation', '')
            ]
            return filtered_substations
        return substations

    def find_substation_in_border(self, border_id: int):
        # Step 1: Fetch the border polygon
        border_polygon = self.get_border_polygon_by_id(border_id)

        # Step 2: Use Overpass to fetch substations inside the polygon
        substations = self.get_substations_in_polygon(border_polygon)

        # Step 3: Handle cases based on number of substations found
        if len(substations['elements']) == 1:
            print("One substation found:", substations['elements'][0])
            return substations['elements'][0]
        elif len(substations['elements']) > 1:
            print(f"Multiple substations found. Applying filters...")
            filtered_substations = self.filter_substations(substations)
            if len(filtered_substations) == 1:
                print("One substation found after filtering:", filtered_substations[0])
                return filtered_substations[0]
            elif len(filtered_substations) == 0:
                raise ValueError("No substations found after filtering.")
            else:
                raise ValueError(f"Still multiple substations found after filtering: {len(filtered_substations)}")
        else:
            raise ValueError("No substations found inside the border.")

# Example usage
gpkg_file_path = './repositories/primary_cabins.gpkg'  # Specify your GPKG file path here
finder = SubstationFinder(gpkg_file_path)

border_id = 124291  # Replace with the border ID you are testing with
try:
    substation = finder.find_substation_in_border(border_id)
    print("Substation found:", substation)
except ValueError as e:
    print(e)
