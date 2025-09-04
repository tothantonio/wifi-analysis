import os

import pandas as pd
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.realpath(__file__))
csv_file = os.path.join(script_dir, '..', 'data', 'processed', 'wifi_cluj_clean.csv')
plots_dir = os.path.join(script_dir, '..', 'output', 'plots')
os.makedirs(plots_dir, exist_ok=True)

df = pd.read_csv(csv_file)

tip_counts = df['tip_retea'].value_counts()
plt.figure(figsize=[6,4])
tip_counts.plot(kind='bar', color=['#4C72B0','#55A868'])
plt.title("Numar retele Wi-fi")
plt.ylabel("Numar retele")
plt.xticks(rotation=0)
plt.tight_layout()
tip_file = os.path.join(plots_dir, "wifi_type.png")
plt.savefig(tip_file)
plt.close()

zona_counts = df['zona'].value_counts().sort_values(ascending=False).head(10)
plt.figure(figsize=(8,5))
zona_counts.plot(kind='bar', color='#FF7F0E')
plt.title('Top 10 zone cu retele Wi-Fi')
plt.ylabel('Numar retele')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
zone_file = os.path.join(plots_dir, 'coverage_by_area.png')
plt.savefig(zone_file)
plt.close()

