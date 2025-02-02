

from services.request_handler import RequestHandler

from shapely import Polygon

print('Starting the program')

# [input variable population]
latitude = 39.9526
longitude = -75.1652

# Creating the square around Philadelphia
polygon_coordinates = [
    (longitude - 0.003, latitude + 0.01),  # Top-left
    (longitude + 0.003, latitude + 0.008),  # Top-right
    (longitude + 0.003, latitude - 0.008),  # Bottom-right
    (longitude - 0.003, latitude - 0.008)   # Bottom-left
]
selected_area_polygon = Polygon(polygon_coordinates)
# [/input variable population]


request_handler = RequestHandler()
request_handler.build_grid(selected_area_polygon)
request_handler.button_clicked()
# Plot the graph on OpenStreetMap
print('Program ended')

# polygons of primary substation <-> read the shapefile <-> ogc files
# openstreetmap for primary cabin coordinates
