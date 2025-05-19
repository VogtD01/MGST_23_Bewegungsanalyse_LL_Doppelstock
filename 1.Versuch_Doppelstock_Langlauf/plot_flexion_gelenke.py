import pandas as pd
import matplotlib.pyplot as plt

# CSV-Datei laden: Anpassen mit deinem Pfad
csv_path = 'Doppelstock_Langlauf/Data/Data_tests/2025-04-08-18-13_IMU_FB_1DV(1).csv'  # z. B. 'IMU_FB_1DV.csv'

# Die eigentlichen Datenzeilen beginnen ab Zeile 3 (Index 2), daher skiprows=2
df = pd.read_csv(csv_path, skiprows=3, sep=';', decimal=',')
print(f"Die Datei '{csv_path}' wurde erfolgreich geladen.")
print(f"Anzahl der Zeilen: {len(df)}")

# Relevante Spalten für Hüfte, Knie, Ellbogen und Sprunggelenk (links und rechts)
winkel_spalten = [
    'LT Hip Flexion (deg)', 'RT Hip Flexion (deg)',
    'LT Knee Flexion (deg)', 'RT Knee Flexion (deg)',
    'LT Elbow Flexion (deg)', 'RT Elbow Flexion (deg)',
    'LT Ankle Dorsiflexion (deg)', 'RT Ankle Dorsiflexion (deg)',
]

# Sicherstellen, dass nur diese Spalten extrahiert werden
winkel_df = df[winkel_spalten]

# Subplots erstellen
fig, axes = plt.subplots(4, 1, figsize=(10, 15), sharex=True)

# Plot für Knie
axes[0].plot(winkel_df['LT Knee Flexion (deg)'], label='Linkes Knie')
axes[0].plot(winkel_df['RT Knee Flexion (deg)'], label='Rechtes Knie')
axes[0].set_title('Knie – Flexion über die Zeit')
axes[0].set_ylabel('Winkel (Grad)')
axes[0].legend()
axes[0].grid()

# Plot für Ellbogen
axes[1].plot(winkel_df['LT Elbow Flexion (deg)'], label='Linker Ellbogen')
axes[1].plot(winkel_df['RT Elbow Flexion (deg)'], label='Rechter Ellbogen')
axes[1].set_title('Ellbogen – Flexion über die Zeit')
axes[1].set_ylabel('Winkel (Grad)')
axes[1].legend()
axes[1].grid()

# Plot für Sprunggelenk
axes[2].plot(winkel_df['LT Ankle Dorsiflexion (deg)'], label='Linkes Sprunggelenk')
axes[2].plot(winkel_df['RT Ankle Dorsiflexion (deg)'], label='Rechtes Sprunggelenk')
axes[2].set_title('Sprunggelenk – Dorsalflexion über die Zeit')
axes[2].set_ylabel('Winkel (Grad)')
axes[2].legend()
axes[2].grid()

# Plot für Hüfte
axes[3].plot(winkel_df['LT Hip Flexion (deg)'], label='Linke Hüfte')
axes[3].plot(winkel_df['RT Hip Flexion (deg)'], label='Rechte Hüfte')
axes[3].set_title('Hüfte – Flexion über die Zeit')
axes[3].set_xlabel('Zeit (in Samples)')
axes[3].set_ylabel('Winkel (Grad)')
axes[3].legend()
axes[3].grid()

# Layout anpassen und anzeigen
plt.tight_layout()
plt.show()