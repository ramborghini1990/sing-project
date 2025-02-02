import geopandas as gpd
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


border_id = 124291  


def main():
    try:
        request_handler = RequestHandler()
        return request_handler.build_grid(124291)
    except Exception as e:
        print("An error occurred:")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
