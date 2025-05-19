import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

# CSV-Datei laden: Anpassen mit deinem Pfad
csv_path = 'Doppelstock_Langlauf/Data/Data_tests/2025-04-08-18-13_IMU_FB_1DV(1).csv'  # z. B. 'IMU_FB_1DV.csv'


# Die eigentlichen Datenzeilen beginnen ab Zeile 3 (Index 2), daher skiprows=2
df = pd.read_csv(csv_path, skiprows=3, sep=';', decimal=',')



# Plot: Einzelne Achsen der Beschleunigung
plt.figure(figsize=(12, 5))
plt.plot(df["time"], df["RT Hand Accel Sensor X (mG)"], label="X-Achse", alpha=0.8)
plt.plot(df["time"], df["RT Hand Accel Sensor Y (mG)"], label="Y-Achse", alpha=0.8)
plt.plot(df["time"], df["RT Hand Accel Sensor Z (mG)"], label="Z-Achse", alpha=0.8)
plt.title("Beschleunigung der rechten Hand (Langlaufstock) – Einzelachsen")
plt.xlabel("Zeit (s)")
plt.ylabel("Beschleunigung (mG)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# Betrag der Beschleunigung berechnen
df["accel_magnitude"] = np.sqrt(
    df["RT Hand Accel Sensor X (mG)"]**2 +
    df["RT Hand Accel Sensor Y (mG)"]**2 +
    df["RT Hand Accel Sensor Z (mG)"]**2
)

# Plot: Gesamtbeschleunigung
plt.figure(figsize=(10, 4))
plt.plot(df["time"], df["accel_magnitude"], color="black")
plt.title("Gesamtbeschleunigung der rechten Hand (Langlaufstock)")
plt.xlabel("Zeit (s)")
plt.ylabel("Betrag der Beschleunigung (mG)")
plt.grid(True)
plt.tight_layout()
plt.show()


# Peaks (Stockeinsätze) erkennen
peaks, _ = find_peaks(df["accel_magnitude"], height=7000, distance=20)

# Plot mit Markierungen
plt.figure(figsize=(12, 5))
plt.plot(df["time"], df["accel_magnitude"], label="Gesamtbeschleunigung", color="black")
plt.plot(df["time"].iloc[peaks], df["accel_magnitude"].iloc[peaks], "ro", label="Stockeinsatz")
plt.title("Erkannte Stockeinsätze über Beschleunigung")
plt.xlabel("Zeit (s)")
plt.ylabel("Beschleunigung (mG)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Zeitpunkte der Einschläge
peak_times = df["time"].iloc[peaks].values

# Zeitabstände zwischen den Einschlägen berechnen
time_differences = np.diff(peak_times)

# Tabelle erstellen
impact_df = pd.DataFrame({
    "Index": peaks,
    "Zeit (s)": peak_times
})

# Zeitabstände als eigene Spalte (vorne bleibt NaN)
impact_df["Δt zum nächsten Einschlag (s)"] = np.append(time_differences, np.nan)

# Ausgabe
print(impact_df)

# Statistik berechnen
mean_dt = np.mean(time_differences)
std_dt = np.std(time_differences)

# Schübe pro Minute berechnen
# Anzahl der Einschläge / Zeitspanne in Minuten
total_time = df["time"].iloc[-1] - df["time"].iloc[0]
shoves_per_minute = len(peaks) / (total_time / 60)

# Ausgabe der Berechnungen
print(f"Mittelwert der Zeitabstände: {mean_dt:.3f} Sekunden")
print(f"Standardabweichung der Zeitabstände: {std_dt:.3f} Sekunden")
print(f"Schübe pro Minute: {shoves_per_minute:.2f}")

# Plot der Verteilung der Zeitabstände (Histogramm)
plt.figure(figsize=(10, 5))
plt.hist(time_differences, bins=20, edgecolor="black", color="lightblue")
plt.title("Verteilung der Zeitabstände zwischen Stockeinsätzen")
plt.xlabel("Zeitabstand (s)")
plt.ylabel("Häufigkeit")
plt.grid(True)
plt.tight_layout()
plt.show()

# Liste für die maximalen und minimalen Winkel
max_min_angles_rom = []

# Für jedes Intervall zwischen den Einschlägen die Gelenkwinkel berechnen
for i in range(len(peaks)-1):
    start_idx = peaks[i]
    end_idx = peaks[i+1]
    
    # Subset für das Intervall zwischen zwei Einschlägen
    interval_df = df.iloc[start_idx:end_idx]
    
    # Max und Min Werte für Knie, Hüfte und Ellbogen in diesem Intervall
    knee_left_min = interval_df["LT Knee Flexion (deg)"].min()
    knee_left_max = interval_df["LT Knee Flexion (deg)"].max()
    knee_right_min = interval_df["RT Knee Flexion (deg)"].min()
    knee_right_max = interval_df["RT Knee Flexion (deg)"].max()
    
    hip_left_min = interval_df["LT Hip Flexion (deg)"].min()
    hip_left_max = interval_df["LT Hip Flexion (deg)"].max()
    hip_right_min = interval_df["RT Hip Flexion (deg)"].min()
    hip_right_max = interval_df["RT Hip Flexion (deg)"].max()
    
    elbow_left_min = interval_df["LT Elbow Flexion (deg)"].min()
    elbow_left_max = interval_df["LT Elbow Flexion (deg)"].max()
    elbow_right_min = interval_df["RT Elbow Flexion (deg)"].min()
    elbow_right_max = interval_df["RT Elbow Flexion (deg)"].max()
    
    # ROM für jedes Gelenk
    knee_left_rom = knee_left_max - knee_left_min
    knee_right_rom = knee_right_max - knee_right_min
    hip_left_rom = hip_left_max - hip_left_min
    hip_right_rom = hip_right_max - hip_right_min
    elbow_left_rom = elbow_left_max - elbow_left_min
    elbow_right_rom = elbow_right_max - elbow_right_min
    
    # Max/Min Werte und ROM als Liste für jedes Intervall
    max_min_angles_rom.append({
        "Knee Left Min": knee_left_min, "Knee Left Max": knee_left_max, "Knee Left ROM": knee_left_rom,
        "Knee Right Min": knee_right_min, "Knee Right Max": knee_right_max, "Knee Right ROM": knee_right_rom,
        "Hip Left Min": hip_left_min, "Hip Left Max": hip_left_max, "Hip Left ROM": hip_left_rom,
        "Hip Right Min": hip_right_min, "Hip Right Max": hip_right_max, "Hip Right ROM": hip_right_rom,
        "Elbow Left Min": elbow_left_min, "Elbow Left Max": elbow_left_max, "Elbow Left ROM": elbow_left_rom,
        "Elbow Right Min": elbow_right_min, "Elbow Right Max": elbow_right_max, "Elbow Right ROM": elbow_right_rom
    })

# Neues DataFrame mit den max/min Werten und ROM
max_min_rom_df = pd.DataFrame(max_min_angles_rom)

# An das impact_df anfügen
impact_df = pd.concat([impact_df, max_min_rom_df], axis=1)


# Ausgabe des erweiterten impact_df
print(impact_df.head())


##############################################teststet

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
axes[0].plot(df["time"], winkel_df['LT Knee Flexion (deg)'], label='Linkes Knie')
axes[0].plot(df["time"], winkel_df['RT Knee Flexion (deg)'], label='Rechtes Knie')
axes[0].set_title('Knie – Flexion über die Zeit')
axes[0].set_ylabel('Winkel (Grad)')
axes[0].legend()
axes[0].grid()

for peak_time in peak_times:
    axes[0].axvline(x=peak_time, color='red', linestyle='--', alpha=0.7, label='Einschlagzeitpunkt')

# Plot für Ellbogen
axes[1].plot(df["time"], winkel_df['LT Elbow Flexion (deg)'], label='Linker Ellbogen')
axes[1].plot(df["time"], winkel_df['RT Elbow Flexion (deg)'], label='Rechter Ellbogen')
axes[1].set_title('Ellbogen – Flexion über die Zeit')
axes[1].set_ylabel('Winkel (Grad)')
axes[1].legend()
axes[1].grid()

for peak_time in peak_times:
    axes[1].axvline(x=peak_time, color='red', linestyle='--', alpha=0.7, label='Einschlagzeitpunkt')


# Plot für Sprunggelenk
axes[2].plot(df["time"], winkel_df['LT Ankle Dorsiflexion (deg)'], label='Linkes Sprunggelenk')
axes[2].plot(df["time"], winkel_df['RT Ankle Dorsiflexion (deg)'], label='Rechtes Sprunggelenk')
axes[2].set_title('Sprunggelenk – Dorsalflexion über die Zeit')
axes[2].set_ylabel('Winkel (Grad)')
axes[2].legend()
axes[2].grid()

for peak_time in peak_times:
    axes[2].axvline(x=peak_time, color='red', linestyle='--', alpha=0.7, label='Einschlagzeitpunkt')

# Plot für Hüfte
axes[3].plot(df["time"], winkel_df['LT Hip Flexion (deg)'], label='Linke Hüfte')
axes[3].plot(df["time"], winkel_df['RT Hip Flexion (deg)'], label='Rechte Hüfte')
axes[3].set_title('Hüfte – Flexion über die Zeit')
axes[3].set_xlabel('Zeit (s)')
axes[3].set_ylabel('Winkel (Grad)')
axes[3].legend()
axes[3].grid()

for peak_time in peak_times:
    axes[3].axvline(x=peak_time, color='red', linestyle='--', alpha=0.7, label='Einschlagzeitpunkt')

# Layout anpassen und anzeigen
plt.tight_layout()
plt.show()