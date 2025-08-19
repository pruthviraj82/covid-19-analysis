import csv
import os
import matplotlib.pyplot as plt
from collections import defaultdict

# Get absolute paths
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, '..', 'data')

# 1. Read CSV Data
def read_csv_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return list(csv.reader(f))

# 2. Load files (update these names if different)
confirmed = read_csv_data(os.path.join(data_dir, 'time_series_covid19_confirmed_global.csv'))
deaths = read_csv_data(os.path.join(data_dir, 'time_series_covid19_deaths_global.csv'))

# 3. Process data
dates = confirmed[0][4:]  # Skip first 4 columns (metadata)
global_cases = [0] * len(dates)
global_deaths = [0] * len(dates)

for row in confirmed[1:]:  # Skip header row
    for i, val in enumerate(row[4:]):
        global_cases[i] += int(float(val)) if val else 0  # Handle empty values

for row in deaths[1:]:
    for i, val in enumerate(row[4:]):
        global_deaths[i] += int(float(val)) if val else 0

# 4. Plot
plt.figure(figsize=(12, 6))
plt.plot(dates[::30], global_cases[::30], label="Confirmed Cases")  # Show every 30th date for clarity
plt.plot(dates[::30], global_deaths[::30], label="Deaths", color='red')
plt.title("Global COVID-19 Trends")
plt.xlabel("Date")
plt.ylabel("Total Count")
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(script_dir, '..', 'global_trends.png'))
plt.show()