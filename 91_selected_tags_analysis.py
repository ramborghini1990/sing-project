from services.osm_data_fetcher import OSMDataFetcher

state = 'Italia'

selected_properties = [
'substation',
'building',
'operator',
'voltage',
'ref:terna',
'utility',
'voltage:secondary',
'voltage:primary',
'disused',
'industrial',
'ref:enel:type:connection',
'abandoned',
'tourism',
'historic',
'plant:source',
'operational_status',
'ruins',
'demolished:building',
'building:disused',
'end_date',
'disused:transformer'
]


osm_data_fetcher = OSMDataFetcher()
final_analysis = osm_data_fetcher.analyze_substations_tags_values_by_state(state, selected_properties)
