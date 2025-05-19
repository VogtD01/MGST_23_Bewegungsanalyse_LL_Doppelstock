import pandas as pd

# CSV-Datei laden: Anpassen mit deinem Pfad
csv_path = 'Doppelstock_Langlauf/Data/Data_tests/2025-04-08-18-13_IMU_FB_1DV(1).csv'  # z. B. 'IMU_FB_1DV.csv'


# Die eigentlichen Datenzeilen beginnen ab Zeile 3 (Index 2), daher skiprows=2
df = pd.read_csv(csv_path, skiprows=3, sep=';', decimal=',')

for i, col in enumerate(df.columns):
    print(f"{i}: {col}")