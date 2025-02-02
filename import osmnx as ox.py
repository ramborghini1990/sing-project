from services.request_handler import RequestHandler

from shapely import Polygon
import osmnx as ox

print('Starting the program')

# [input variable population]
latitude = 39.944932938780276
longitude = -75.16377258263189

# Creating the square around Philadelphia
polygon_coordinates = [
    (longitude - 0.005, latitude + 0.01),  # Top-left
    (longitude + 0.005, latitude + 0.01),  # Top-right
    (longitude + 0.005, latitude - 0.01),  # Bottom-right
    (longitude - 0.005, latitude - 0.01)   # Bottom-left
]
selected_area_polygon = Polygon(polygon_coordinates)
# [/input variable population]

# import overpy
import overpass

# Initialize Overpass API
api = overpass.API()

# Define the coordinates for Philadelphia
min_lat = 39.8670041
max_lat = 40.1379919
min_lon = -75.280284
max_lon = -74.955762

# Define the query
query = f"""
node["power"="transformer"](poly:"{latitude - 0.1} {longitude - 0.1} {latitude - 0.1} {longitude + 0.1} {latitude + 0.1} {longitude + 0.1} {latitude + 0.1} {longitude - 0.1} {latitude - 0.1} {longitude - 0.1}");
out geom;
"""

# Send the query
response = api.Get(query)
print(response)

# Print the{ results}
# for node in response.nodes:
#     print(f"Found substation at {node}")

