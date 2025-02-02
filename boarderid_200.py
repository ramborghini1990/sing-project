import fiona

# Path to your GPKG file
gpkg_file = './repositories/primary_cabins.gpkg'

# List all layers in the GPKG file
with fiona.Env():
    with fiona.open(gpkg_file, layer=None) as src:
        layers = fiona.listlayers(gpkg_file)

# Print the available layers
print("Available layers:", layers)
