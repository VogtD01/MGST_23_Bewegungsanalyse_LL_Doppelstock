# MGST\_23\_Bewegungsanalyse\_LL\_Doppelstock

**Ein Projekt von Dominic Vogt, Lennard Zaschke und Paul Krajewski**
**MCI Innsbruck**

## 📘 Projektbeschreibung

Dieses Projekt beschäftigt sich mit der **Bewegungsanalyse des Doppelstockschubs im Skilanglauf**. Ziel war es, anhand von IMU-Daten (Inertial Measurement Units) automatisiert **Bewegungszyklen zu erkennen** und daraus **biomechanisch relevante Kennwerte** zu berechnen, darunter:

* **Range of Motion (ROM)** von Hüfte, Knie, Ellbogen und Sprunggelenk
* **Zeitabstände zwischen Schüben**
* **Schübe pro Minute** als Frequenzmaß

Zusätzlich wurde untersucht, ob sich Unterschiede in der Bewegungsausführung bei **flachem Gelände** im Vergleich zu **bergauf** zeigen.

---

## 🗂️ Projektstruktur

```
MGST_23_Bewegungsanalyse_LL_Doppelstock/
│
├── Data/                                ← Rohdaten der IMU-Messungen (.csv)
├── Data_nach_Auswertung/                ← Zyklusweise ausgewertete CSV-Dateien
├── Ergebnisse_Plots/                    ← Automatisch generierte Visualisierungen (PNG/PDF)
│
├── Auswertung_1_Schritt.ipynb           ← Einlesen der Rohdaten, Peak-Erkennung, ROM-Berechnung
├── Auswertung_2_Schritt.ipynb           ← Vergleichsplots, ROM-Verläufe, Zusammenfassungen
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🔍 Auswertung in zwei Schritten

Die Analyse wurde in zwei Schritten durchgeführt:

1. **Auswertung\_1\_Schritt.ipynb**
   → Einlesen der IMU-CSV-Dateien, automatisches Erkennen der **Stockeinsätze (Peaks)** und Berechnung der relevanten ROM- und Zeitkennwerte pro Zyklus.
   Die Ergebnisse werden dabei als CSV-Dateien zur weiteren Auswertung abgespeichert.

2. **Auswertung\_2\_Schritt.ipynb**
   → Einlesen der vorbereiteten CSVs und Durchführung der **eigentlichen Analyse**:

   * Vergleich von Gelenkbewegungen über Geländeformen
   * Rechts-/Links-Vergleiche (explorativ)
   * ROM-Verläufe über normierte Schubzyklen
   * Visualisierung von Mittelwerten & Standardabweichungen
   * Export der Ergebnisse als Tabellen und Diagramme

---

## ⚙️ Installation

1. Projekt herunterladen:

```sh
git clone https://github.com/VogtD01/MGST_23_Bewegungsanalyse_LL_Doppelstock.git
cd MGST_23_Bewegungsanalyse_LL_Doppelstock
```

2. Virtuelle Umgebung erstellen & aktivieren:

```sh
python -m venv .venv
# Aktivieren unter Windows:
.venv\Scripts\activate
# Oder unter macOS/Linux:
source .venv/bin/activate
```

3. Abhängigkeiten installieren:

```sh
pip install -r requirements.txt
```

---

## 🤖 Hinweis zur Unterstützung durch KI

Zur Unterstützung beim Coden haben wir auch KI-Tools wie GitHub Copilot und ChatGPT verwendet – zum Beispiel für die Strukturierung von Funktionen, Automatisierungen und Plots.

