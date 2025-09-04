import os

import folium
import pandas as pd
from folium.plugins import HeatMap

script_dir = os.path.dirname(os.path.realpath(__file__))
csv_file = os.path.join(script_dir, '..', 'data', 'processed', 'wifi_cluj_clean.csv')
maps_dir = os.path.join(script_dir, '..', 'output', 'maps')
os.makedirs(maps_dir, exist_ok=True)

df = pd.read_csv(csv_file)

lat_center = df['lat'].mean()
lon_center = df['lon'].mean()

map = folium.Map(location=[lat_center, lon_center], zoom_start=13)

color_dict = {
    'ClujWifi': 'green',
    'Wifi4EU': 'blue'
}

for _, row in df.iterrows():
    color = color_dict.get(row['tip_retea'], 'red')

    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=5,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.7,
        popup=f"{row['SSID']} ({row['tip_retea']}, {row['zona']})"
    ).add_to(map)

map_interactive = os.path.join(maps_dir, 'wifi_cluj_interactive.html')
map.save(map_interactive)
print(f"Mapa interactiva salvata in {map_interactive}")

map_heat = folium.Map(location=[lat_center, lon_center], zoom_start=13)
heat_data = df[['lat', 'lon']].values.tolist()
HeatMap(heat_data, radius = 15).add_to(map_heat)

heat_map_file = os.path.join(maps_dir, 'wifi_cluj_heat_map.html')
map_heat.save(heat_map_file)
print(f"Heatmap salvata in {heat_map_file}")
