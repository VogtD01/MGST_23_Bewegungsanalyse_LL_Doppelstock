import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


"""Validierung der Flexion und Extension der Gelenke

Die Daten werden aus einer CSV-Datei geladen, die Gelenkwinkel werden extrahiert und in einem Plot dargestellt.
Die Gelenkwinkel umfassen Flexion und Extension für Ellenbogen, Knie und Hüfte.
Die Daten stammen von einem Noraxon MyoMotion-System und sind in Grad angegeben.
Um die sinnhaftigkeit der daten zu prüfen wird jeweils flexion und extension in einem gelenk gegeneinander geplottet
"""

# CSV-Datei laden: Anpassen mit deinem Pfad
csv_path = 'Doppelstock_Langlauf/Data/Data_tests/2025-04-08-18-13_IMU_FB_1DV(1).csv'  # z. B. 'IMU_FB_1DV.csv'

# Die eigentlichen Datenzeilen beginnen ab Zeile 3 (Index 2), daher skiprows=2
df = pd.read_csv(csv_path, skiprows=3, sep=';', decimal=',')
# Überprüfen, ob die Datei korrekt geladen wurde    

print(f"Die Datei '{csv_path}' wurde erfolgreich geladen.")
print(f"Anzahl der Zeilen: {len(df)}")


# Spaltennamen bereinigen (Leerzeichen entfernen, falls nötig)
df.columns = [col.strip() for col in df.columns]

# Relevante Spaltennamen
columns = {
    'LT Elbow Flexion': 'LT Elbow Flexion (deg)',
    'LT Elbow Extension': 'Noraxon MyoMotion-Joints-Elbow LT-Extension (deg)',
    'RT Elbow Flexion': 'RT Elbow Flexion (deg)',
    'RT Elbow Extension': 'Noraxon MyoMotion-Joints-Elbow RT-Extension (deg)',
    'LT Knee Flexion': 'LT Knee Flexion (deg)',
    'LT Knee Extension': 'Noraxon MyoMotion-Joints-Knee LT-Extension (deg)',
    'RT Knee Flexion': 'RT Knee Flexion (deg)',
    'RT Knee Extension': 'Noraxon MyoMotion-Joints-Knee RT-Extension (deg)',
    'LT Hip Flexion': 'LT Hip Flexion (deg)',
    'RT Hip Flexion': 'RT Hip Flexion (deg)'
}

# DataFrame mit relevanten Spalten
df_angles = df[list(columns.values())].copy()
#df_angles = df_angles.head(2000)  # auf 2000 Zeilen beschränken

# Plot erstellen
plt.figure(figsize=(14, 10))
plot_titles = [
    ('LT Elbow Flexion', 'LT Elbow Extension'),
    ('RT Elbow Flexion', 'RT Elbow Extension'),
    ('LT Knee Flexion', 'LT Knee Extension'),
    ('RT Knee Flexion', 'RT Knee Extension'),
    ('LT Hip Flexion', None),
    ('RT Hip Flexion', None),
]

for i, (flex_key, ext_key) in enumerate(plot_titles):
    plt.subplot(3, 2, i+1)
    plt.plot(df_angles[columns[flex_key]], label='Flexion')
    if ext_key:
        plt.plot(df_angles[columns[ext_key]], label='Extension')
    plt.title(f"{flex_key.split()[0]} {flex_key.split()[1]}")
    plt.xlabel("Sample")
    plt.ylabel("Winkel (deg)")
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()