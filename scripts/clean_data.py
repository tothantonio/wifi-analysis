import json
import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, '..', 'data', 'raw', 'wifi_cluj_raw.json')

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

print("Info about data:")
print(df.info())

df['lat'] = df['lat'].astype(float)
df['lon'] = df['lon'].astype(float)

def extract_zone(descriere):
    if ',' in descriere:
        return descriere.split(',')[0].strip()
    else:
        return descriere.strip()

df['zona'] = df['descriere'].apply(extract_zone)

df['tip_retea'] = df['SSID'].apply(lambda x: 'ClujWifi' if 'Cluj Wifi Free' in x else 'WIFI4EU')

print(df['tip_retea'].value_counts())
print(df['zona'].value_counts())

print("Latitudine - Min:", df['lat'].min(), "Max:", df['lat'].max())
print("Longitudine - Min:", df['lon'].min(), "Max:", df['lon'].max())

df.to_csv("wifi_cluj_clean.csv", index=False, encoding='utf-8')
print("datele au fost salvate")


