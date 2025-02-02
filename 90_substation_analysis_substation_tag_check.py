from services.osm_data_fetcher import OSMDataFetcher

state = 'Italia'


osm_data_fetcher = OSMDataFetcher()
final_analysis = osm_data_fetcher.analyze_substations_tags_by_state(state)
