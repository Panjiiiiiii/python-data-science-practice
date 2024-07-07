import pandas as pd
import os


#example
download_folder = os.path.expanduser("~/Downloads")
file_path = os.path.join(download_folder, "covid_19_indonesia_time_series_all.csv")

#csv_reader
df = pd.read_csv(file_path, delimiter=",")
print(df)

#checking missing value
print(df.isnull().sum(), "\n")

#checking duplicate value
print(df.duplicated().sum())