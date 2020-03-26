# https://pomber.github.io/covid19/timeseries.json
import pandas as pd
from pandas.io.json import json_normalize

df = pd.read_json("https://pomber.github.io/covid19/timeseries.json")

df_time = pd.DataFrame(columns=["date", "confirmed", "deaths", "recovered", "country"])
for c in df.columns.unique().tolist():
    tmp =  json_normalize(df[c]).set_index("date").reset_index()
    tmp["country"] = c
    df_time = pd.concat([df_time, tmp])


df_time.reset_index(drop=True, inplace=True)
df_time["date"] = pd.to_datetime(df_time["date"])
df_time.columns = ['Date', 'Confirmed', 'Deaths', 'Recovered', 'Country']

df_time.to_csv("covid_19_clean_complete_json.csv", index=None)