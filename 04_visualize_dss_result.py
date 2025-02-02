import folium
import os

# Function to parse georeferenced .dss file
def parse_georef_dss(file_path):
    georef_data = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            name = parts[0]
            longitude = float(parts[1])
            latitude = float(parts[2])
            georef_data[name] = (latitude, longitude)
    return georef_data

# Function to parse linked .dss file
def parse_linked_dss(file_path):
    linked_data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for j, line in enumerate(lines):
            lines[j] = line.replace('\\n', '')
            lines[j] = line.replace('\n', '')

        for line in lines:
            if line == '':
                continue
            parts = line.strip().split()
            linked_data.append(parts[0])
    return linked_data

# File paths (replace with the actual paths to your .dss files)
georef_dss_path = './output/coordinates.dss'
linked_dss_path = './output/test.dss'

# Parse the .dss files
georef_data = parse_georef_dss(georef_dss_path)
linked_data = parse_linked_dss(linked_dss_path)

# Create a map centered around the average coordinates
map_center = [39.945, -75.163]  # Adjust the center as needed
map_ = folium.Map(location=map_center, zoom_start=16)

# Add markers for the georeferenced data
for name, coords in georef_data.items():
    folium.Marker(coords, popup=name, icon=folium.Icon(color='blue')).add_to(map_)

# Add markers for the linked data if they exist in georeferenced data
for name in linked_data:
    if name in georef_data:
        folium.Marker(georef_data[name], popup=name, icon=folium.Icon(color='green')).add_to(map_)

# Save the map to an HTML file
map_.save('linked_substation_map.html')
