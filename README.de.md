# 11-06-2025 UPDATE:
**🌟 Update der Modellspeicherung für CipherCore 🌟**

Gute Nachrichten für Portabilität und Modellorganisation!

CipherCore wird nun alle Modelle vom Hugging Face Hub direkt in den `checkpoints`-Ordner im Hauptverzeichnis der Anwendung herunterladen und speichern.

**Was das für Sie bedeutet:**
*   **Vollständige Portabilität:** Die App und ihre Modelle sind jetzt vollständig eigenständig. Verschieben Sie den CipherCore-Ordner und Ihre Modelle ziehen mit!
*   **Dedizierter Modellspeicher:** Von dieser App heruntergeladene Modelle werden nicht mehr in Ihrem globalen Hugging Face-Cache-Verzeichnis (typischerweise in Ihrem Benutzerordner) abgelegt.

**Hinweis:** Diese Änderung gilt für Modelle, die ab dieser Version von CipherCore heruntergeladen werden. Modelle, die sich bereits in Ihrem globalen Hugging Face-Cache befinden, werden nicht automatisch verschoben.

# CipherCore SD1.5 - SCHNELLE Lokale Stable Diffusion 1.5 Bildgenerator-Web-UI (CPU & GPU)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Willkommen beim CipherCore Stable Diffusion 1.5 Generator! Diese benutzerfreundliche Gradio-Webanwendung ermöglicht es Ihnen, mühelos Bilder mit verschiedenen Stable Diffusion 1.5-Modellen kostenlos lokal auf Ihrem eigenen PC zu generieren. Egal, ob Sie lokale Modelle haben oder beliebte Modelle vom Hugging Face Hub bevorzugen, dieses Tool bietet eine einfache Benutzeroberfläche, um Ihre Kreativität auf Ihrer CPU oder GPU zu entfesseln.

Dieses Projekt ist für **Windows**-Benutzer konzipiert, die eine einfache Erfahrung durch benutzerfreundliche Batch-Dateien suchen, sowie für andere Plattformen oder fortgeschrittene Benutzer, die ein bisschen Schmerz genießen, manuelle Einrichtungsoptionen bietet.

## Screenshot der Anwendung:
![Screenshot der CipherCore Stable Diffusion 1.5 Benutzeroberfläche](images/ciphercore01.png)

---

## ✨ Funktionen
- **Flexible Modellauswahl:**
  - Laden Sie Ihre eigenen Stable Diffusion 1.5-Modelle (im `diffusers`-Format) aus einem lokalen `./checkpoints`-Verzeichnis.
  - Greifen Sie direkt aus der App auf eine kuratierte Liste beliebter SD1.5-Modelle zu (Modelle werden bei der ersten Verwendung lokal heruntergeladen und zwischengespeichert).
- **Geräteunabhängig:**
  - Führen Sie die Inferenz auf Ihrer **CPU** aus. (Inferenzzeit ca. 4:55 mit einem i5 der 10. Generation – nicht schlecht für einen Toaster).
  - Nutzen Sie Ihre **NVIDIA GPU** für eine deutlich schnellere Generierung (Euler 30 Schritte = 8 Sek. mit 6 GB VRAM). CUDA-Magie erforderlich.
- **Umfassende Steuerung:**
  - **Positive & Negative Prompts:** Leiten Sie die KI mit detaillierten Beschreibungen dessen, was Sie wollen (und was nicht).
  - **Inferenzschritte (Inference Steps):** Steuern Sie die Anzahl der Entrauschungsschritte, denn 20 fühlt sich manchmal einfach nicht wie eine Glückszahl an.
  - **CFG-Skala (CFG Scale):** Passen Sie an, wie stark das Bild Ihrem Prompt entsprechen soll – oder auch nicht. Leben Sie ein bisschen.
  - **Scheduler:** Experimentieren Sie mit verschiedenen Sampling-Algorithmen (Euler, DPM++ 2M, DDPM, LMS), bis Sie Ihre persönliche Geschmacksrichtung des Chaos finden.
  - **Bildgrößen:** Wählen Sie aus den Standard-SD1.5-Auflösungen, plus einer "hire.fix"-Option (interpretiert als 1024x1024, weil die Leute das sowieso meistens meinen).
  - **Seed-Steuerung:** Legen Sie einen bestimmten Seed für reproduzierbare Ergebnisse fest. Oder verwenden Sie -1 und sehen Sie, was das Universum entscheidet.
- **Benutzerfreundliche Oberfläche:**
  - Saubere und intuitive Gradio-Benutzeroberfläche.
  - Organisierte Steuerelemente mit erweiterten Einstellungen, die ordentlich versteckt sind – wie Geheimnisse.
  - Direkte Bildanzeige mit Download- und Freigabeoptionen.
- **Sicherheit geht vor (Hinweis):** Der eingebaute Sicherheitsprüfer ist in dieser Version **deaktiviert**, um maximale kreative Freiheit zu ermöglichen. Verantwortungsvoll nutzen. (Wir sehen Sie.)

---

## 🔥 Warum CipherCore?
Im Gegensatz zu einigen anderen UIs (*hust* Forge) ist **CipherCore auf Geschwindigkeit ausgelegt** – und das nicht nur auf dem Papier.

In einem direkten Vergleichstest mit **Stable Diffusion 1.5**, mit dem **gleichen Modell**, den **gleichen Einstellungen**, dem **gleichen Seed** und auf der **gleichen reinen CPU-Maschine**:

| Web-UI | Schritte | Scheduler | Zeit pro Schritt | Gesamtzeit |
|----------------|----------|-----------|-----------------|------------|
| **CipherCore** | 20 | Euler | 20,72 Sek. | **6:54** |
| **Forge** | 20 | Euler | 34,78 Sek. | **11:35** |

Das ist fast **doppelt so schnell** – und das, ohne Ihre Maschine den arkanen Göttern des Python-Overheads zu opfern.

CipherCore ist **stark optimiert** für sowohl CPU- als auch GPU-Umgebungen:
- Schlanker Start und effiziente Speichernutzung.
- Saubere Gradio-Architektur ohne überflüssigen Ballast im Hintergrund oder unnötigen Schnickschnack.
- Blitzschnelles lokales Caching und Modell-Handling.
- Optimiert für Systeme mit wenig VRAM (besonders auf der GPU). Ja, sogar Ihre arme 6-GB-Karte.

Erwarten Sie noch bessere Ergebnisse auf der GPU – tatsächliche Benchmarks folgen in Kürze, sobald eine GPU verfügbar ist, die nicht von Minern oder Gamern gekapert wurde.

---

## 🚀 Voraussetzungen
- **Windows-Betriebssystem:** Die mitgelieferten Batch-Dateien (`.bat`) sind für Windows. Für andere Betriebssysteme folgen Sie den nachstehenden manuellen Einrichtungsschritten (Warnung: erfordert tatsächliches Tippen).
- **Python:** 3.8 oder höher. Stellen Sie sicher, dass Python installiert und zum PATH Ihres Systems hinzugefügt wurde (normalerweise eine Option während der Installation). Sie können Python von [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) herunterladen.
- **Git:** (Erforderlich für die manuelle Einrichtung und Aktualisierung) Zum Klonen des Repositories.
- **Hardware:**
  - Eine moderne CPU ist erforderlich.
  - Für GPU-Beschleunigung (optional, aber für die Geschwindigkeit dringend empfohlen) ist eine kompatible NVIDIA-GPU mit aktuellen CUDA-Treibern erforderlich. Mindestens 6–8 GB VRAM werden für die 512x512-Generierung empfohlen, mehr für größere Formate.
  - **Wichtig:** Die korrekte CUDA-Version für Ihre Treiber ist entscheidend. Verwenden Sie `nvidia-smi` in der Eingabeaufforderung, um die mit Ihrem Treiber kompatible CUDA-Version zu überprüfen. Oder raten Sie wild drauf los – ganz wie Sie möchten.
- **Internetverbindung:** Erforderlich für das Herunterladen von Modellen vom Hugging Face Hub und für Updates. Sorry, es generiert (noch) keine Träume offline.

---

## 📦 Einfache Einrichtung (Windows - Herunterladen & Ausführen)
Dies ist die empfohlene Methode für die meisten Windows-Benutzer. **Es werden zwei separate Setup-Skripte bereitgestellt:** eines für die CPU-Inferenz und eines für die GPU-Inferenz.

1.  **Projekt herunterladen:**
    -   Gehen Sie zur GitHub-Repository-Seite: `https://github.com/Raxephion/CipherCore-WebUI`
    -   Klicken Sie auf den grünen „Code“-Button.
    -   Klicken Sie auf „Download ZIP“.
2.  **ZIP-Datei entpacken:** Entpacken Sie die heruntergeladene ZIP-Datei an einem Ort auf Ihrem Computer (z. B. Ihrem Dokumentenordner oder dem Desktop). Dadurch wird ein Ordner wie `CipherCore-SD1.5-Image-Generator-main` (oder ähnlich) erstellt. Benennen Sie ihn um, wenn Ihnen danach ist.
3.  **Ihr Setup-Skript auswählen:**
    -   **Für CPU-Inferenz:** Führen Sie `setup-CPU.bat` aus. Dies installiert die CPU-Version von PyTorch.
    -   **Für GPU-Inferenz:** Führen Sie `setup-GPU.bat` aus. Dies versucht, die CUDA-fähige Version von PyTorch zu installieren.
4.  **Das Setup-Skript ausführen:**
    -   Navigieren Sie in den entpackten Ordner.
    -   **Doppelklicken Sie entweder auf `setup-CPU.bat` oder `setup-GPU.bat`**, je nachdem, ob Sie CPU- oder GPU-Inferenz wünschen.
    -   Ein Eingabeaufforderungsfenster wird geöffnet. Folgen Sie den Anweisungen im Fenster. Dieses Skript erstellt eine virtuelle Python-Umgebung (`venv`), installiert alle notwendigen Kernabhängigkeiten und die passende Version von PyTorch.
    -   **Wichtig:** Lesen Sie die Ausgabe in der Eingabeaufforderung während und nach Abschluss des Skripts sorgfältig durch.
        -   **Wenn Sie `setup-GPU.bat` verwenden und die CUDA-Installation fehlschlägt:** Das Skript gibt Anweisungen zur Fehlerbehebung bei der CUDA-Installation oder wie Sie als Fallback die CPU-Version von PyTorch installieren können. Es ist keine Schande, zur CPU zurückzukehren. Okay, vielleicht ein bisschen.
5.  **Lokale Modelle vorbereiten (Optional):**
    -   Erstellen Sie im entpackten Projektordner ein Verzeichnis mit dem Namen `checkpoints` (falls das Setup-Skript es nicht erstellt hat).
    -   Legen Sie Ihre Stable Diffusion 1.5-Modelle (im `diffusers`-Format – jedes Modell ist ein Ordner mit Dateien wie `model_index.json`, `unet/`, `vae/` usw.) in das `checkpoints`-Verzeichnis.

---

## 🔄 Anwendung aktualisieren (Windows - Einfache Methode)
Um den neuesten Code, Abhängigkeitsupdates und aktualisierte Modelle aus diesem Repository nach der einfachen Einrichtung zu erhalten:
- Navigieren Sie zum Projektordner.
- Doppelklicken Sie auf `update.bat`, um es auszuführen.
- Ein Eingabeaufforderungsfenster wird geöffnet, holt die neuesten Änderungen aus dem GitHub-Repository und aktualisiert die Python-Pakete in Ihrer virtuellen Umgebung. Herzlichen Glückwunsch, Sie sind jetzt ein kleines bisschen moderner.

---

## ▶️ Anwendung ausführen (Windows - Einfache Methode)
Sobald die Einrichtung abgeschlossen ist, starten Sie die Gradio-Web-UI durch einen Doppelklick auf die `run.bat`-Datei im Projektordner.
- Ein Eingabeaufforderungsfenster wird geöffnet, die Umgebung aktiviert und die Anwendung gestartet.
- Ein Browserfenster sollte sich automatisch mit der Anwendung öffnen (oder eine lokale URL wird in der Konsole angezeigt, normalerweise `http://127.0.0.1:7860`).
- Wenn nichts passiert: Überprüfen Sie Ihre Firewall, Ihr Antivirenprogramm und Ihre Lebensentscheidungen.

---

## ⚙️ Manuelle Einrichtung (Windows - Git Clone)
1.  **Repository klonen:**
    ```bash
    git clone https://github.com/Raxephion/CipherCore-SD1.5-Image-Generator-.git
    cd CipherCore-SD1.5-Image-Generator-
    ```
2.  **Mit Batch-Dateien fortfahren:** Fahren Sie fort, indem Sie den obigen Anweisungen zur Einrichtung, zu den Modellen, zum Ausführen und zum Aktualisieren folgen.

---

## 🛠️ Manuelle Einrichtung, Ausführung & Aktualisierung (Für Linux/macOS oder fortgeschrittene Benutzer)
1.  **Repository klonen:**
    ```bash
    git clone https://github.com/Raxephion/CipherCore-SD1.5-Image-Generator-.git
    cd CipherCore-SD1.5-Image-Generator-
    ```
2.  **Virtuelle Umgebung erstellen und aktivieren:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3.  **Abhängigkeiten installieren:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **PyTorch installieren:**
    -   **CPU:**
        ```bash
        pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
        ```
    -   **CUDA (GPU):** Besuchen Sie [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/) und wählen Sie die passende CUDA-Version.
5.  **App ausführen:**
    ```bash
    python main.py
    ```
6.  **Aktualisieren:**
    ```bash
    git pull
    pip install -r requirements.txt --upgrade
    ```

---

## ⚙️ Deinstallation
Löschen Sie einfach den Ordner. Das ist alles. Keine seltsamen Registry-Einträge. Keine dunklen Rituale.

---

## 📄 Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](https://opensource.org/licenses/MIT) Datei für Details.
