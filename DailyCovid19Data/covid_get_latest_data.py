import pandas as pd
import wget
import os

print("Getting the latest data...")
urls = ['https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv', 
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv', 
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv']
for url in urls:
    filename = wget.download(url)

conf_df = pd.read_csv('time_series_19-covid-Confirmed.csv')
deaths_df = pd.read_csv('time_series_19-covid-Deaths.csv')
recv_df = pd.read_csv('time_series_19-covid-Recovered.csv')

print("\n")
dates = conf_df.columns[4:]
print("Last Date: ", dates[-1])
conf_df_long = conf_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
                            value_vars=dates, var_name='Date', value_name='Confirmed')

deaths_df_long = deaths_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
                            value_vars=dates, var_name='Date', value_name='Deaths')

recv_df_long = recv_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
                            value_vars=dates, var_name='Date', value_name='Recovered')

full_table = pd.concat([conf_df_long, deaths_df_long['Deaths'], recv_df_long['Recovered']], 
                       axis=1, sort=False)

full_table = full_table[full_table['Province/State'].str.contains(',')!=True]
full_table.to_csv('covid_19_clean_complete.csv', index=False)
print("\n")
print("Total Rows:", full_table.shape[0])
print("Done..!")

for c in ['time_series_19-covid-Confirmed.csv', 'time_series_19-covid-Deaths.csv', 'time_series_19-covid-Recovered.csv']:
	os.remove(c)
