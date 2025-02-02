import geopandas as gpd

# Load GeoJSON file
gdf = gpd.read_file('./repositories/primary_cabins.geojson')

# Save to a GeoPackage file
gdf.to_file('./repositories/primary_cabins.gpkg', driver='GPKG')
