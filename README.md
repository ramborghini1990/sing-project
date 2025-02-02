<<<<<<< HEAD
<<<<<<< HEAD
# synth-grids
=======

# Substation Analysis Project

# Description
This project focuses on analyzing and visualizing substations within a specified geographic area. It includes various scripts to filter, retrieve, and visualize substation data using different tools and libraries.

# Methods
1. `00_filter_substations.py`
=======
# synth-grids
# Substation Analysis Project

## Description
This project focuses on analyzing and visualizing substations within a specified geographic area. It includes various scripts to filter, retrieve, and visualize substation data using different tools and libraries.

## Methods

### 1. `00_filter_substations.py`
>>>>>>> 3f83077c115e82c8bedccc0c0e341a7640f1d1a0
- **Description**: Filters substations within a specified polygon around Philadelphia.
- **Parameters**: 
  - `latitude`: Latitude of the center point.
  - `longitude`: Longitude of the center point.
- **Returns**: Substations within the specified polygon.

<<<<<<< HEAD
2. `get_buildings.py`
=======
### 2. `get_buildings.py`
>>>>>>> 3f83077c115e82c8bedccc0c0e341a7640f1d1a0
- **Description**: Retrieves building data within a specified polygon around Philadelphia.
- **Parameters**: 
  - `latitude`: Latitude of the center point.
  - `longitude`: Longitude of the center point.
- **Returns**: Building data within the specified polygon.

<<<<<<< HEAD
3. `03_build_grid.py`
=======
### 3. `03_build_grid.py`
>>>>>>> 3f83077c115e82c8bedccc0c0e341a7640f1d1a0
- **Description**: Builds a grid within a specified polygon around Philadelphia.
- **Parameters**: 
  - `latitude`: Latitude of the center point.
  - `longitude`: Longitude of the center point.
- **Returns**: Grid data within the specified polygon.

<<<<<<< HEAD
4. `03_save_opendss.py`
=======
### 4. `03_save_opendss.py`
>>>>>>> 3f83077c115e82c8bedccc0c0e341a7640f1d1a0
- **Description**: Builds a grid and saves it in OpenDSS format.
- **Parameters**: 
  - `latitude`: Latitude of the center point.
  - `longitude`: Longitude of the center point.
- **Returns**: Grid data in OpenDSS format.

<<<<<<< HEAD
5. `04_visualize_dss_result.py`
=======
### 5. `04_visualize_dss_result.py`
>>>>>>> 3f83077c115e82c8bedccc0c0e341a7640f1d1a0
- **Description**: Visualizes the results of the DSS analysis on a map.
- **Parameters**: 
  - `georef_dss_path`: Path to the georeferenced DSS file.
  - `linked_dss_path`: Path to the linked DSS file.
- **Returns**: HTML file with the map visualization.

<<<<<<< HEAD
6. `05_select_polygon.py`
=======
### 6. `05_select_polygon.py`
>>>>>>> 3f83077c115e82c8bedccc0c0e341a7640f1d1a0
- **Description**: Selects a polygon from a shapefile and retrieves substation data within it.
- **Parameters**: 
  - `file_path`: Path to the shapefile.
- **Returns**: Substation data within the selected polygon.

<<<<<<< HEAD
7. `90_substation_analysis_substation_tag_check.py`
=======
### 7. `90_substation_analysis_substation_tag_check.py`
>>>>>>> 3f83077c115e82c8bedccc0c0e341a7640f1d1a0
- **Description**: Analyzes substation tags by state.
- **Parameters**: 
  - `state`: Name of the state.
- **Returns**: Analysis of substation tags.

<<<<<<< HEAD
8. `91_selected_tags_analysis.py`
=======
### 8. `91_selected_tags_analysis.py`
>>>>>>> 3f83077c115e82c8bedccc0c0e341a7640f1d1a0
- **Description**: Analyzes selected substation tags by state.
- **Parameters**: 
  - `state`: Name of the state.
  - `selected_properties`: List of selected properties to analyze.
- **Returns**: Analysis of selected substation tags.

<<<<<<< HEAD
9. `92_selected_substation_distribution.py`
=======
### 9. `92_selected_substation_distribution.py`
>>>>>>> 3f83077c115e82c8bedccc0c0e341a7640f1d1a0
- **Description**: Analyzes the distribution of selected substation tags by state.
- **Parameters**: 
  - `state`: Name of the state.
  - `selected_properties`: List of selected properties to analyze.
- **Returns**: Distribution analysis of selected substation tags.

<<<<<<< HEAD
10. `93_distinct_operator.py`
=======
### 10. `93_distinct_operator.py`
>>>>>>> 3f83077c115e82c8bedccc0c0e341a7640f1d1a0
- **Description**: Retrieves distinct operators from a CSV file and filters them.
- **Parameters**: 
  - `file_path`: Path to the CSV file.
  - `operators_to_exclude`: Set of operators to exclude.
- **Returns**: Filtered list of distinct operators.

<<<<<<< HEAD
11. `101_convert_geojson_to_geopackage.py`
=======
### 11. `101_convert_geojson_to_geopackage.py`
>>>>>>> 3f83077c115e82c8bedccc0c0e341a7640f1d1a0
- **Description**: Converts a GeoJSON file to a GeoPackage file.
- **Parameters**: 
  - `geojson_path`: Path to the GeoJSON file.
- **Returns**: GeoPackage file.

<<<<<<< HEAD
12. `201_final.py`
=======
### 12. `201_final.py`
>>>>>>> 3f83077c115e82c8bedccc0c0e341a7640f1d1a0
- **Description**: Builds a grid using a specified border ID.
- **Parameters**: 
  - `border_id`: ID of the border.
- **Returns**: Grid data.

<<<<<<< HEAD
13. `202_final_flask.py`
=======
### 13. `202_final_flask.py`
>>>>>>> 3f83077c115e82c8bedccc0c0e341a7640f1d1a0
- **Description**: Flask application to build a grid using a specified border ID and optional GeoJSON data.
- **Parameters**: 
  - `border_id`: ID of the border.
  - `substation_coordinates`: GeoDataFrame of substation coordinates.
  - `building_geojson`: GeoDataFrame of building data.
  - `streets_geojson`: GeoDataFrame of street data.
  - `load_profiles`: DataFrame of load profiles.
- **Returns**: JSON response with the grid data.

<<<<<<< HEAD
14. `202_osm.py`
=======
### 14. `202_osm.py`
>>>>>>> 3f83077c115e82c8bedccc0c0e341a7640f1d1a0
- **Description**: Finds substations within a specified border polygon using Overpass API.
- **Parameters**: 
  - `border_id`: ID of the border.
- **Returns**: Substation data within the specified border polygon.

<<<<<<< HEAD
15. `boarderid_200.py`
=======
### 15. `boarderid_200.py`
>>>>>>> 3f83077c115e82c8bedccc0c0e341a7640f1d1a0
- **Description**: Lists all layers in a GeoPackage file.
- **Parameters**: 
  - `gpkg_file`: Path to the GeoPackage file.
- **Returns**: List of available layers.

<<<<<<< HEAD
16. `import osmnx as ox.py`
=======
### 16. `import osmnx as ox.py`
>>>>>>> 3f83077c115e82c8bedccc0c0e341a7640f1d1a0
- **Description**: Retrieves transformer data within a specified polygon around Philadelphia using Overpass API.
- **Parameters**: 
  - `latitude`: Latitude of the center point.
  - `longitude`: Longitude of the center point.
- **Returns**: Transformer data within the specified polygon.
