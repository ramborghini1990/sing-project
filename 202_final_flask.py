import geopandas as gpd
import pandas as pd
import json
from shapely.geometry import shape
import sys
sys.path.append('./services')
import os
import model
from osm_data_fetcher import OSMDataFetcher
from model import Model  
from primary import PrimaryModel  
from secondary import SecondaryModel  
from request_handler import RequestHandler  
from fuzzywuzzy import fuzz
from flask import Flask, request, jsonify

app = Flask(__name__)

request_handler = RequestHandler()


@app.route('/build_grid', methods=['POST'])
def build_grid():
    '''
    Input: substation border id: int, building_geojson: geojson (optional)
    Output: grid geojson
    '''
    try:
        border_id, substation_coordinates, building_geojson, streets_geojson, loads = _read_input(request)

        result = request_handler.build_grid(border_id, substation_coordinates, building_geojson, streets_geojson, loads)

        return jsonify({"result": result}), 200
    
    except Exception as e:
        print("An error occurred:")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500



def _read_input(request):
    try:
        data = request.get_json()

        if 'border_id' not in data:
            return jsonify({"error": "border_id is required"}), 400
        
        border_id = data['border_id']
        substation_coordinates = None
        building_geojson = None
        streets_geojson = None
        load_profiles = None

        if 'substation_coordinates' in data:
            geojson = data['substation_coordinates']
            if 'features' in geojson and len(geojson['features']) > 0:
                substation_coordinates = gpd.GeoDataFrame.from_features(geojson['features'])
                
                substation_coordinates['geometry'] = substation_coordinates['geometry'].apply(shape)
                substation_coordinates.set_geometry('geometry', inplace=True)
                
                substation_coordinates.set_crs(epsg=4326, inplace=True)

        if 'building_geojson' in data:
            geojson = data['building_geojson']
            if 'features' in geojson and len(geojson['features']) > 0:
                building_geojson = gpd.GeoDataFrame.from_features(geojson['features'])
                
                building_geojson['geometry'] = building_geojson['geometry'].apply(shape)
                building_geojson.set_geometry('geometry', inplace=True)
                
                building_geojson.set_crs(epsg=4326, inplace=True)
                if 'id' not in building_geojson.columns:
                    building_geojson['id'] = [feature.get('id') for feature in geojson['features']]
        
        if 'streets_geojson' in data:
            geojson = data['streets_geojson']
            if 'features' in geojson and len(geojson['features']) > 0:
                streets_geojson = gpd.GeoDataFrame.from_features(geojson['features'])
                
                streets_geojson['geometry'] = streets_geojson['geometry'].apply(shape)
                streets_geojson.set_geometry('geometry', inplace=True)
                
                streets_geojson.set_crs(epsg=4326, inplace=True)

        if 'load_profiles' in data:
            load_profiles = pd.DataFrame(data['load_profiles'])

        return border_id, substation_coordinates, building_geojson, streets_geojson, load_profiles
    
    except Exception as ex:
        print('Input data does not have the expected format.')
        print(str(ex.args))
        return jsonify({"error": "Invalid input format"}), 400


if __name__ == "__main__":
    app.run(debug=True)