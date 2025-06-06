# CipherCore SD1.5 – Schnelle Stable Diffusion 1.5 Lokale Bildgenerator Web-UI (CPU & GPU)

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Willkommen beim CipherCore Stable Diffusion 1.5 Generator! Diese benutzerfreundliche Gradio-Webanwendung ermöglicht es Ihnen, mühelos Bilder mit verschiedenen Stable Diffusion 1.5 Modellen zu generieren – kostenlos und lokal auf Ihrem eigenen PC. Egal, ob Sie lokale Modelle verwenden oder beliebte Modelle vom Hugging Face Hub bevorzugen, dieses Tool bietet eine einfache Oberfläche, um Ihrer Kreativität auf Ihrer CPU oder GPU freien Lauf zu lassen.

Dieses Projekt ist für **Windows**-Benutzer konzipiert, die eine einfache Bedienung durch leicht verständliche Batch-Dateien suchen. Es bietet aber auch manuelle Setup-Optionen für andere Plattformen oder fortgeschrittene Benutzer.

## Anwendungs-Screenshot:

![Screenshot der CipherCore Stable Diffusion 1.5 UI](images/ciphercore01.png)

## ✨ Funktionen

*   **Flexible Modellauswahl:**
    *   Laden Sie Ihre eigenen Stable Diffusion 1.5 Modelle (im `diffusers`-Format) aus einem lokalen `./checkpoints`-Verzeichnis.
    *   Greifen Sie direkt aus der App auf eine kuratierte Liste beliebter SD1.5-Modelle zu (Modelle werden beim ersten Gebrauch heruntergeladen und lokal zwischengespeichert).
*   **Geräteunabhängig:**
    *   Führen Sie Inferenz auf Ihrer **CPU** aus. (Inferenzzeit ca. 4:55 mit einem i5 der 10. Generation)
    *   Nutzen Sie Ihre **NVIDIA GPU** für eine deutlich schnellere Generierung (Euler 30 Schritte = 8 Sekunden mit 6 GB VRAM) (erfordert die Installation der CUDA-fähigen PyTorch-Version).
*   **Umfassende Kontrolle:**
    *   **Positive & Negative Prompts:** Leiten Sie die KI mit detaillierten Beschreibungen dessen, was Sie möchten (und was nicht).
    *   **Inference Steps:** Steuern Sie die Anzahl der Denoising-Schritte.
    *   **CFG Scale:** Passen Sie an, wie stark sich das Bild an Ihren Prompt halten soll.
    *   **Schedulers:** Experimentieren Sie mit verschiedenen Sampling-Algorithmen (Euler, DPM++ 2M, DDPM, LMS).
    *   **Bildgrößen:** Wählen Sie aus Standard-SD1.5-Auflösungen sowie einer "hire.fix"-Option (interpretiert als 1024x1024).
    *   **Seed Control:** Legen Sie einen bestimmten Seed für reproduzierbare Ergebnisse fest oder verwenden Sie -1 für zufällige Generierung.
*   **Benutzerfreundliche Oberfläche:**
    *   Saubere und intuitive Gradio-UI.
    *   Organisierte Steuerelemente mit erweiterten Einstellungen in einem Akkordeon für ein aufgeräumteres Aussehen.
    *   Direkte Bildanzeige mit Download- und Freigabeoptionen.
*   **Sicherheit geht vor (Hinweis):** Der integrierte Sicherheits-Checker ist in dieser Version **deaktiviert**, um maximale kreative Freiheit zu ermöglichen. Bitte seien Sie sich der Inhalte bewusst, die Sie generieren.

## 🚀 Voraussetzungen

*   **Windows-Betriebssystem:** Die bereitgestellten Batch-Dateien (`.bat`) sind für Windows. Für andere Betriebssysteme folgen Sie den manuellen Setup-Schritten unten.
*   **Python:** 3.8 oder höher. Stellen Sie sicher, dass Python installiert und zum PATH Ihres Systems hinzugefügt wurde (normalerweise eine Option während der Installation). Sie können Python von [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) herunterladen.
*   **Git:** (Erforderlich für manuelle Einrichtung und Aktualisierung) Zum Klonen des Repository.
*   **Hardware:**
    *   Eine moderne CPU ist erforderlich.
    *   Für GPU-Beschleunigung (optional, aber für Geschwindigkeit dringend empfohlen) eine kompatible NVIDIA-GPU mit aktuellen CUDA-Treibern. Mindestens 6–8 GB VRAM werden für die Generierung von 512x512 empfohlen, mehr für größere Größen. **Wichtig:** Die richtige CUDA-Version für Ihre Treiber ist entscheidend. Verwenden Sie `nvidia-smi` in der Eingabeaufforderung, um die mit Ihrem Treiber kompatible CUDA-Version zu überprüfen.
*   **Internetverbindung:** Erforderlich zum Herunterladen von Modellen vom Hugging Face Hub und für Aktualisierungen.

## 📦 Einfache Einrichtung (Windows – Herunterladen & Ausführen)

Dies ist die empfohlene Methode für die meisten Windows-Benutzer. **Es werden zwei separate Setup-Skripte bereitgestellt:** eines für CPU-Inferenz und eines für GPU-Inferenz.

1.  **Projekt herunterladen:**
    *   Gehen Sie zur GitHub-Repository-Seite: `https://github.com/Raxephion/CipherCore-WebUI`
    *   Klicken Sie auf die grüne Schaltfläche "Code".
    *   Klicken Sie auf "Download ZIP".
2.  **ZIP entpacken:** Entpacken Sie die heruntergeladene ZIP-Datei an einen Ort auf Ihrem Computer (z. B. Ihren Dokumente-Ordner oder Desktop). Dadurch wird ein Ordner wie `CipherCore-SD1.5-Image-Generator-main` (oder ähnlich) erstellt. Benennen Sie ihn bei Bedarf um.
3.  **Wählen Sie Ihr Setup-Skript:**
    *   **Für CPU-Inferenz:** Führen Sie `setup-CPU.bat` aus. Dadurch wird die CPU-Version von PyTorch installiert.
    *   **Für GPU-Inferenz:** Führen Sie `setup-GPU.bat` aus. Dadurch wird versucht, die CUDA-fähige Version von PyTorch zu installieren.

4.  **Setup-Skript ausführen:**
    *   Navigieren Sie in den entpackten Ordner.
    *   **Doppelklicken Sie entweder auf `setup-CPU.bat` oder `setup-GPU.bat`**, je nachdem, ob Sie CPU- oder GPU-Inferenz wünschen.
    *   Ein Eingabeaufforderungsfenster wird geöffnet. Befolgen Sie die Anweisungen im Fenster. Dieses Skript erstellt eine virtuelle Python-Umgebung (`venv`), installiert alle erforderlichen Kernabhängigkeiten und installiert die entsprechende Version von PyTorch.
    *   **Wichtig:** Lesen Sie die Ausgabe in der Eingabeaufforderung während und nach Abschluss des Skripts sorgfältig durch.
        *   **Wenn bei Verwendung von `setup-GPU.bat` die CUDA-Installation fehlschlägt:** Das Skript enthält Anweisungen zur Fehlerbehebung bei der CUDA-Installation oder zur Installation der CPU-Version von PyTorch als Fallback. Stellen Sie sicher, dass Sie eine kompatible NVIDIA-GPU, die richtigen Treiber haben und dass Sie Ihre CUDA-Version mit `nvidia-smi` überprüft haben. Möglicherweise müssen Sie `setup-GPU.bat` bearbeiten, um die richtige CUDA-Version anzugeben.

5.  **Lokale Modelle vorbereiten (Optional):**
    *   Erstellen Sie im extrahierten Projektordner ein Verzeichnis namens `checkpoints` (falls das Setup-Skript es nicht erstellt hat).
    *   Platzieren Sie Ihre Stable Diffusion 1.5 Modelle (im `diffusers`-Format – d. h. jedes Modell ist ein Ordner mit Dateien wie `model_index.json`, `unet/`, `vae/` usw.) im Verzeichnis `checkpoints`.
        Beispielstruktur:
        ```
        YourProjectFolder/
        ├── checkpoints/
        │   ├── my-custom-model-1/
        │   │   ├── model_index.json
        │   │   ├── unet/
        │   │   └── ...
        │   └── another-local-model/
        │       └── ...
        ├── main.py
        ├── requirements.txt
        ├── setup-CPU.bat
        ├── setup-GPU.bat
        ├── run.bat
        ├── update.bat
        ├── images/              <-- Dieser Ordner sollte existieren
        │   └── ciphercore01.png   <-- Ihre Bilddatei sollte hier sein
        └── ...
        ```

## 🔄 Aktualisieren der Anwendung (Windows – Einfache Methode)

So erhalten Sie nach der einfachen Einrichtung den neuesten Code, Abhängigkeitsaktualisierungen und aktualisierte Modelle aus diesem Repository:

*   Navigieren Sie zum Projektordner.
*   Suchen Sie die Datei mit dem Namen `update.bat`.
*   **Doppelklicken Sie auf `update.bat`**, um sie auszuführen.
*   Ein Eingabeaufforderungsfenster wird geöffnet, zieht die neuesten Änderungen aus dem GitHub-Repository und aktualisiert die Python-Pakete in Ihrer virtuellen Umgebung.
*   **Wichtig:** Dies setzt voraus, dass Sie keine lokalen Änderungen vorgenommen haben, die mit den Repository-Aktualisierungen in Konflikt stehen. Wenn `git pull` fehlschlägt, müssen Sie möglicherweise Merge-Konflikte manuell beheben oder lokale Änderungen verwerfen.

## ▶️ Ausführen der Anwendung (Windows – Einfache Methode)

Sobald das Setup abgeschlossen ist, starten Sie die Gradio-Web-UI, indem Sie im Projektordner auf die Datei `run.bat` doppelklicken.

*   Ein Eingabeaufforderungsfenster wird geöffnet, aktiviert die Umgebung und startet die Anwendung.
*   Ein Browserfenster sollte sich automatisch mit der Anwendung öffnen (oder eine lokale URL wird in der Konsole angegeben, normalerweise `http://127.0.0.1:7860`).

---

## ⚙️ Manuelle Einrichtung (Windows – Git-Clone)

Diese Methode ist für Windows-Benutzer, die mit Git vertraut sind.

1.  **Repository klonen:** Öffnen Sie die Eingabeaufforderung oder PowerShell, navigieren Sie zu dem Ort, an dem Sie das Projekt herunterladen möchten, und führen Sie Folgendes aus:

    ```bash
    git clone https://github.com/Raxephion/CipherCore-SD1.5-Image-Generator-.git
    cd CipherCore-SD1.5-Image-Generator-
    ```

    *(Hinweis: Wenn Sie in einen anderen Verzeichnisnamen geklont haben, ersetzen Sie `CipherCore-SD1.5-Image-Generator-` oben durch Ihren gewählten Verzeichnisnamen.)*
2.  **Mit Batch-Dateien fortfahren:** Fahren Sie fort, indem Sie **Schritt 3 (Wählen Sie Ihr Setup-Skript)**, **Schritt 4 (Führen Sie das Setup-Skript aus)** (für Ihre *eigenen* Checkpoints), **Ausführen** und **Aktualisieren** aus dem Abschnitt **📦 Einfache Einrichtung (Windows – Herunterladen & Ausführen)** oben befolgen. Stellen Sie sicher, dass Sie den Ordner `images` manuell erstellen und `ciphercore01.png` hinzufügen, wenn Sie diese Methode verwenden und diese noch nicht im geklonten Repository vorhanden sind.

## 🛠️ Manuelle Einrichtung, Ausführen und Aktualisieren (Für Linux/macOS oder fortgeschrittene Benutzer)

Wenn Sie nicht unter Windows sind oder einen manuellen Befehlszeilenansatz bevorzugen:

1.  **Repository klonen:**

    ```bash
    git clone https://github.com/Raxephion/CipherCore-SD1.5-Image-Generator-.git
    cd CipherCore-SD1.5-Image-Generator-
    ```

2.  **Erstellen und Aktivieren einer virtuellen Umgebung:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Abhängigkeiten installieren (einschließlich PyTorch):**

    *   Installieren Sie die Kernabhängigkeiten (dies umfasst `gradio`, `diffusers`, `transformers`, `huggingface_hub`, `Pillow`):

        ```bash
        pip install -r requirements.txt
        ```

    *   Installieren Sie PyTorch: **Dieser Schritt ist entscheidend und hängt von Ihrer Hardware ab.**

        *   **Nur für CPU:**

            ```bash
            pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
            ```

        *   **Für NVIDIA GPU mit CUDA (Empfohlen für Geschwindigkeit):** Führen Sie zuerst `nvidia-smi` aus, um die richtige CUDA-Version für Ihr System zu ermitteln. Suchen Sie dann auf der PyTorch-Website den entsprechenden Befehl für Ihre CUDA-Version: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/). Beispiel für CUDA 11.8:

            ```bash
            pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
            ```

4.  **Lokale Modelle vorbereiten (Optional):** Befolgen Sie Schritt 4 aus dem Abschnitt **📦 Einfache Einrichtung (Windows – Herunterladen & Ausführen)** oben (der Teil über den `checkpoints`-Ordner).
5.  **Anwendung ausführen:**

    ```bash
    python main.py
    ```

    Stellen Sie sicher, dass Ihre virtuelle Umgebung aktiviert ist (`source venv/bin/activate`), bevor Sie diesen Befehl ausführen.
6.  **Manuelles Aktualisieren:**

    *   Navigieren Sie in Ihrem Terminal zum Projektverzeichnis.
    *   Stellen Sie sicher, dass Ihre virtuelle Umgebung aktiviert ist (`source venv/bin/activate`).
    *   Ziehen Sie den neuesten Code: `git pull`
    *   Aktualisieren Sie die Abhängigkeiten: `pip install -r requirements.txt --upgrade`
    *   Deaktivieren Sie die Umgebung: `deactivate`

## ⚙️ Deinstallation:

1.  **Löschen Sie das Hauptverzeichnis (den Ordner) – diese App ist vollständig portabel.**

## 📄 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert – siehe die Datei [LICENSE](https://opensource.org/licenses/MIT) für Details.
