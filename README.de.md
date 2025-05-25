# CipherCore SD1.5 – SCHNELLE Stable Diffusion 1.5 Bildgenerierung lokal (CPU & GPU)

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Willkommen beim **CipherCore Stable Diffusion 1.5 Generator**! Diese benutzerfreundliche Gradio-Webanwendung ermöglicht es dir, mühelos Bilder mit verschiedenen Stable Diffusion 1.5-Modellen **kostenlos und lokal auf deinem eigenen PC** zu erzeugen. Egal ob du lokale Modelle nutzt oder beliebte Modelle vom Hugging Face Hub bevorzugst – dieses Tool bietet dir eine einfache Oberfläche, um deiner Kreativität freien Lauf zu lassen – auf **CPU oder GPU**.

Das Projekt richtet sich an **Windows-Nutzer**, die eine unkomplizierte Erfahrung mit praktischen Batch-Dateien wünschen. Für andere Plattformen oder fortgeschrittene Benutzer gibt es auch eine manuelle Einrichtungsmöglichkeit.

---

## Screenshot der Anwendung

![Screenshot der CipherCore Stable Diffusion 1.5 Oberfläche](images/ciphercore01.png)

---

## ✨ Funktionen

- **Flexible Modellauswahl:**
  - Lade deine eigenen Stable Diffusion 1.5-Modelle (im `diffusers`-Format) aus dem lokalen Verzeichnis `./checkpoints`.
  - Greife direkt aus der App auf eine kuratierte Liste beliebter SD1.5-Modelle zu (Modelle werden beim ersten Start heruntergeladen und lokal zwischengespeichert).
- **Geräteunabhängig:**
  - Bilderzeugung auf deiner **CPU** möglich.
  - Nutze deine **NVIDIA GPU** für deutlich schnellere Ergebnisse (benötigt die CUDA-fähige Version von PyTorch). **Standardmäßig wird die CPU-Version installiert – eine Anleitung zum GPU-Upgrade liegt bei.**
- **Umfassende Steuerung:**
  - **Positive & Negative Prompts:** Gib detailliert an, was du im Bild haben möchtest – und was nicht.
  - **Inference Steps:** Bestimme, wie viele Denoising-Schritte durchgeführt werden.
  - **CFG-Skala:** Passe an, wie stark das Bild deinem Prompt folgen soll.
  - **Scheduler-Auswahl:** Teste verschiedene Sampling-Algorithmen (Euler, DPM++ 2M, DDPM, LMS).
  - **Bildgrößen:** Wähle Standardauflösungen für SD1.5 oder die „hire.fix“-Option (interpretiert als 1024x1024).
  - **Seed-Kontrolle:** Nutze einen festen Seed für reproduzierbare Ergebnisse oder `-1` für Zufall.
- **Benutzerfreundliche Oberfläche:**
  - Saubere und intuitive Gradio-UI.
  - Aufgeräumte Bedienelemente, erweiterte Einstellungen in einem Akkordeon versteckt.
  - Bilder direkt anzeigen, herunterladen oder teilen.
- **Hinweis zur Sicherheit:** Der integrierte Sicherheitsfilter ist **deaktiviert**, um maximale kreative Freiheit zu ermöglichen. Bitte sei dir der Verantwortung bei der Generierung bewusst.

---

## 🚀 Voraussetzungen

- **Windows-Betriebssystem:** Die mitgelieferten `.bat`-Dateien sind für Windows gedacht. Für andere Systeme siehe weiter unten (manuelle Einrichtung).
- **Python:** Version 3.8 oder höher. Stelle sicher, dass Python installiert ist und zur PATH-Umgebungsvariable hinzugefügt wurde (Option während der Installation). Download: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
- **Git:** (erforderlich für manuelle Einrichtung und Updates)
- **Hardware:**
  - Moderner Prozessor erforderlich.
  - Für GPU-Beschleunigung: Kompatible NVIDIA-GPU mit aktuellen CUDA-Treibern. Mindestens 6–8 GB VRAM für 512×512-Bilder empfohlen, mehr für höhere Auflösungen.
- **Internetverbindung:** Notwendig für Modell-Downloads vom Hugging Face Hub und Updates.

---

## 📦 Einfache Einrichtung (Windows – Download & Start)

**Empfohlene Methode für die meisten Windows-Nutzer:**

1. **Projekt herunterladen:**
   - Gehe zur GitHub-Seite: `https://github.com/Raxephion/CipherCore-WebUI`
   - Klicke auf „Code“ > „Download ZIP“.
2. **ZIP-Datei entpacken:**  
   Entpacke die ZIP-Datei an einen beliebigen Ort (z. B. Dokumente oder Desktop). Ein Ordner wie `CipherCore-SD1.5-Image-Generator-main` wird erstellt.
3. **Setup-Skript ausführen:**
   - Öffne den Ordner.
   - Finde die Datei `setup.bat`.
   - **Doppelklick auf `setup.bat`** zum Start.
   - Es öffnet sich ein Terminalfenster mit Anweisungen. Das Skript erstellt eine virtuelle Python-Umgebung, installiert alle nötigen Abhängigkeiten und die **CPU-Version von PyTorch**.
   - **Wichtig:** Lies die Hinweise im Terminal sorgfältig durch – dort steht auch, wie du manuell auf die GPU-Version umsteigen kannst.
4. **Lokale Modelle vorbereiten (optional):**
   - Erstelle einen `checkpoints`-Ordner im Projektverzeichnis (falls `setup.bat` dies nicht automatisch gemacht hat).
   - Platziere deine SD1.5-Modelle im `diffusers`-Format dort hinein.

   Beispielstruktur:
