import pandas as pd
import os


#example
download_folder = os.path.expanduser("~/Downloads")
file_path = os.path.join(download_folder, "covid_19_indonesia_time_series_all.csv")

#csv_reader
df = pd.read_csv(file_path, delimiter=",")
print(df)

#dropping (dropna())
print(df.dropna(axis=0, inplace=True))

#imputation (fillna())
print(df.fillna(value=df.Population.mean(), inplace=True))

#interpolation
interpolate = df.interpolate(method='linear', limit_direction='forward', inplace=True)
print(interpolate)
