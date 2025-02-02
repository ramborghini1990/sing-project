from services.osm_data_fetcher import OSMDataFetcher

state = 'Italia'

selected_properties = [
'substation',
]


osm_data_fetcher = OSMDataFetcher()
final_analysis = osm_data_fetcher.analyze_substations_tags_values_by_state_distribution(state, selected_properties)
