# nas_dirselector

## Inhaltsverzeichnis:
- [DirSelector.py](#dirselectorpy)
- [directories.txt](#directories.txt)
- [requirements.txt](#requirements.txt)
- [Anweisungen zur Installation / Einrichtung](#anweisungen-zur-installation--einrichtung)

  
## DirSelector.py

Ist ein Python-Skript, das die Verwaltung von heruntergeladene Dateien vereinfacht. DirSelector erkennt automatisch den Verzeichnispfad des Download-Verzeichnisses und reagiert auf neue Dateien, die dort erscheinen. Mit einfachen Tastaturbefehlen können Sie die heruntergeladene Dateien aus einer frei gestaltebaren Liste von Verzeichnisse unkompliziert verschieben und umbenennen. Neue Ordner und ".tmp" Files werden ignoriert. 

### Bedienung:

Damit das Skript funktioniert, muss es ausgeführt werden. 
Ausführen kann man es über die Kommandozeile (CLI). Mit `cd Dateipfad` bewegen Sie sich in den Ordner, in dem das Skript gespeichert und mit `python dirselector.py` in Windows (`python3 dirselector.py` für macOS/Linux) führen Sie es aus.

Wichtig! Beim **herunterladen** von Dateien, diese **NICHT umbenennen**!
Mit CTRL+C wird das Skript abgebrochen. 
    

## directories.txt

Hier können sie Ihre Liste von Verzeichnisse im folgenden Format selber frei gestalten:
   
    "Nummer/Bezeichnung, Dateipfad"

    z.B. "1, C:\\Benutzername\\Bilder"
    oder "mathe, H:\\Schule\\AntonGraff\\Mathe"

Das Skript erkennt ein Verzeichnis pro Zeile.
Leere Zeile werden ignoriert.
Dateipfade von Verzeichnisse finden Sie mit Rechtsklick im gewünschten Ordner und dann in Eigenschaften unter "Ort:".
Um Änderungen in dieser Datei vorzunehmen, muss DirSelector.py neu gestartet werden.

## requirements.txt

Diese Datei dürfen Sie ignorieren oder nach der Installation/Einrichtung des Skripts auch löschen.

## Anweisungen zur Installation / Einrichtung:


1. Auf dem GitHub repository (https://github.com/bi-it-nas/nas_dirselector) in der Abteilung "<> Code" auf dem grünen Knopf "<> Code" drücken und dann die ZIP Datei herunterladen und in Ihrem Computer entpacken.
2. Lade Python von "python.org/downloads" herunter und installieren es. **Wichtig:** Beim Installieren das Kästchen "Add python to PATH" ankreuzen". 
3. Anschliessend in der Kommandozeile mit `cd Dateipfad` (zB. `cd C:\Users\DeinBenutzername\Desktop\nas_dirselector`) in den entpackten Ordner bewegen und mit `pip install -r requirements.txt` die nötige Pakete installieren. 
4. Die Text-Datei "directories.txt" soll anschliessend mit einem Text-Editor nach Ihren Wünschen gestaltet werden. Damit DirSelector.py richtig funktioniert, müssen Sie auf die Formatierung achten (Format: "number,directory_path", auf Deutsch: "Nummer/Bezeichnung,Verzeichnispfad"). Mehr Infos dazu finden Sie oben bei "directories.txt".
5. In der Kommandozeile sollen Sie sich in den Ordner bewegen, in dem das Skript gespeichert ist (cd ordnerpfad) und mit `python dirselector.py` für Windows und `python3 dirselector.py` für macOS/Linux.

## Fehlerbehebung

Überprüfe, ob:

- "directories.txt" richtig formatiert ist.

