import geopandas as gpd

class SubstationBorderRepo:

    file_path = None

    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def fetch_substation_border(self, border_id: int):
        gdf = gpd.read_file(self.file_path, layer='primary_cabins')
        border = gdf[gdf['OBJECTID'] == border_id]
        if border.empty:
            raise ValueError(f"No border found with OBJECTID {border_id}")
        return border.geometry.iloc[0]