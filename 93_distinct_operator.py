from services.osm_data_fetcher import OSMDataFetcher
from services.osm_data_fetcher import names

osmDataFetcher = OSMDataFetcher()

distinct_operators = osmDataFetcher.get_distinct_operators('./repositories/italia_distribution_substations.csv')

# print(distinct_operators)



# compared_operator = osmDataFetcher.compare_operators_with_names(distinct_operators, names)

# print(f'compared operators: {compared_operator}')

operators_to_exclude = {'Trigno Energy', 'Aerorossa', 'IVPC', 'AE-EW Alperia', 'AE-EW', 'Biomasse Italia', 'HERA', 'Hera', 'HERA S.p.A.', 'Iren', 'Iren Energia', 'Pitagora', 'Erg Hydro', 'Erg Eolica Ginestre', 'Pietragalla Eolico','AGC Flat Glass Italia', 'nan', 'Daunia Serracapriola', 'E-Werk Villnöß','SET', 'AGSM Verona', 'AGSM Produzione', 'E2I Energie Speciali', 'Tessenderlo', 'Toto', 'Edison S.p.A.', 'Dolomiti Edison Energy', 'Edison', 'Dolomiti Energia', 'Ferrania', 'Airl Liquide', 'AIM Vicenza', 'TERNA S.p.A.', 'Terna S.p.A.', 'Solland Silicon', 'Compagnia Valdostana Acque', 'Acea Distribuzione', 'Acea', 'Acea Energia', 'Siet', 'Enerbiella', 'Barberini', 'Tecnoparco', 'Alerion', 'Cartiere Monterosa', 'Fiume Santo', 'Astea SPA', 'Serravalle Energy', 'Aem Cremona', 'AEM Cremona', 'AEM Torino Distribuzione', 'Imes', 'Caffaro', 'Sogin', 'Alto Calore Servizi', 'Fiera Milano', 'Euratom', 'ENAS', 'Isab', 'Fortore Energia', 'Libeccio', 'AIR Mezzolombardo', 'Siot', 'Acquedotto Lucano', 'EP Produzione', 'Veronagest', 'CESI', 'SE Hydropower', 'Enipower', 'Polioli', 'Atena', 'RFI', 'Maltemi Energia', 'Green Energy', 'Fiat', 'Italgen', 'Selnet'}

filtered_df = osmDataFetcher.filter_operators('./repositories/italia_distribution_substations.csv', operators_to_exclude)
print(filtered_df)