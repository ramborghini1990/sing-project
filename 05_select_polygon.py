import geopandas as gpd
from shapely.geometry import box
import requests
import json
import numpy as np

from services.osm_data_fetcher import OSMDataFetcher


# Read the shapefile
file_path = './repositories/ireti_torino/ireti_torino.shp' 
data = gpd.read_file(file_path)

# Select a geometry (could be Polygon or MultiPolygon)
geometry = data.geometry[1]

osm_data_fetcher = OSMDataFetcher()
osm_data_fetcher.get_substations_by_polygons(geometry)
