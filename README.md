# MGST\_23\_Bewegungsanalyse\_LL\_Doppelstock

**Ein Projekt von Dominic Vogt, Lennard Zaschke und Paul Krajewski**
**MCI Innsbruck**

## 📘 Projektbeschreibung

Dieses Projekt beschäftigt sich mit der **Bewegungsanalyse des Doppelstockschubs auf Rollski** anhand von IMU-Daten (Inertial Measurement Units).
Ziel war es, **Bewegungszyklen automatisch zu erkennen** und daraus **biomechanisch relevante Kennwerte** wie Range of Motion (ROM) und Schubfrequenz zu analysieren.

---

## 🧪 Analysefokus

* Vergleich der Gelenkbewegung (ROM) von **Hüfte, Knie, Ellbogen und Sprunggelenk**
* Unterschiede zwischen **flachem** und **bergigem Gelände**
* Vergleich zwischen **Anfängern** und einem **erfahrenen Langläufer**
* Analyse der **Schubfrequenz** und **Konsistenz** der Bewegungsausführung
* Zeitliche **Normierung & Interpolation** zur besseren Vergleichbarkeit

---

## 🗂️ Projektstruktur

```
MGST_23_Bewegungsanalyse_LL_Doppelstock/
│
├── Data/                       # Rohdaten der IMU-Messungen (CSV)
├── Data_nach_Auswertung/      # pro Aufzeichnung ausgewertete CSV-Dateien
├── Ergebnisse_Plots/          # Visualisierungen (PNG, PDF)
├── Rohdaten_Noraxon/          
│
├── Auswertung_1_Schritt.ipynb # Peak-Erkennung, ROM-Berechnung, Datenspeicherung
├── Auswertung_2_Schritt.ipynb # Vergleichsplots, Normalisierung, Statistiken
├── Präsentation_BA_MGST_23_...pptx  # Präsentation mit Analyse & Interpretation
│
├── README.md
└── requirements.txt
```

---

## 📈 Auswertungsschritte

### 🔹 Schritt 1: Rohdaten verarbeiten

Notebook: `Auswertung_1_Schritt.ipynb`

* Einlesen der IMU-CSV-Dateien
* Automatische Erkennung der **Stockeinsätze (Peaks)**
* Definition eines Schubzyklus: **von Stockeinsatz zu Stockeinsatz**
* Berechnung:

  * ROM pro Gelenk (L/R & gemittelt)
  * Schubfrequenz (Schübe/Min)
  * Zeitabstände und Zyklusstatistiken
* Speichern der ausgewerteten Daten als CSV-Dateien

---

### 🔹 Schritt 2: Analyse & Visualisierung

Notebook: `Auswertung_2_Schritt.ipynb`

* Darstellung der **ROM-Verläufe ohne Normierung** (pro Zyklus)
* Entscheidung zur **Normierung & Interpolation**, da Vergleichbarkeit sonst eingeschränkt
* **Normierte ROM-Verläufe (0–100 % Schubverlauf)** mit Mittelwert & SD
* Vergleich:

  * Anfänger vs. Profi
  * Flach vs. Berg
  * Bewegungskonsistenz (SD)
* Export der Plots und Tabellen für Präsentation & Bericht


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

## 🗣️ Präsentation & Ergänzungen

Die finale **PowerPoint-Präsentation** mit Analyse und Interpretation befindet sich im Repository:
📄 `Präsentation_BA_MGST_23_VZ_Bewegungsanalyse_LL_Doppelstock.pptx`

Nach der Präsentation wurden noch **3 zusätzliche Folien** ergänzt, um den Ablauf der **Zeit-Normierung und Interpolation** besser zu visualisieren – da dies im Vortrag teilweise **für Verständnisprobleme gesorgt hat**.

---

## 🤖 Hinweis zur Unterstützung durch KI

Zur Unterstützung beim Coden haben wir auch KI-Tools wie GitHub Copilot und ChatGPT verwendet – zum Beispiel für die Strukturierung von Funktionen, Automatisierungen und Plots.



