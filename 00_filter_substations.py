from services.request_handler import RequestHandler

from shapely import Polygon

print('Starting the program')

# [input variable population]
latitude = 39.9526
longitude = -75.1652

# Creating the square around Philadelphia
polygon_coordinates = [
    (longitude - 0.05, latitude + 0.05),  # Top-left
    (longitude + 0.05, latitude + 0.05),  # Top-right
    (longitude + 0.05, latitude - 0.05),  # Bottom-right
    (longitude - 0.05, latitude - 0.05)   # Bottom-left
]
selected_area_polygon = Polygon(polygon_coordinates)
# [/input variable population]


request_handler = RequestHandler()
request_handler.get_substations_in_polygon(selected_area_polygon)

print('Program ended')