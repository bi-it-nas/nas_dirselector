import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

# Findet Download-Ordner
def get_download_folder():
    return str(Path.home() / "Downloads")

# Importiert Verzeichnisliste aus directories.txt
def load_directories(file_path='directories.txt'):
    directories = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
            
                # ignoriert leere Zeile
                if not line or line.startswith('#'):
                    continue
                parts = line.split(',')
                # Überprüft, ob die Verzeichnisse richtig formatiert sind
                if len(parts) == 2:
                    key, path = parts
                    directories[key] = path
                else:
                    print(f"Achtung: Zeile '{line}' ist nicht richtig formatiert. Richtiges Format: 'nummer,ordnerpfad'\nOrdnernamen sollten KEIN Komma enthalten.")
    except FileNotFoundError:
        print(f"Fehlermeldung: 'directories.txt' Konnte nicht gefunden werden. \nÜberprüfen Sie, dass diese Datei sich im gleichen Ordner wie das Skript befindet \noder erstellen Sie eine 'directories.txt Datei mit einer Liste von Verzeichnisse mit dem Format 'zahl/bezeichnung,verzeichnispfad'. \nPro Zeile wird ein Verzeichnis erkannt. ")
        exit(1)
    return directories


class FileHandler(FileSystemEventHandler):
    def __init__(self, directories):
        self.directories = directories
    
    def on_created(self, event):
        # Ignoriert Verzeichnisse
        if event.is_directory:
            return
        
        file_path = event.src_path

        if os.path.splitext(file_path)[1] == ".tmp":
            return
        else:
            print(f"Neue Datei erkannt: {file_path}")

            # Bewegen und umbennen fortfahren
            try:
                self.move_and_rename(file_path)
            except FileNotFoundError:
                print("Leider kann ich die Datei nicht mehr finden. Überprüfen Sie, ob sie umgenannt, umplatziert oder gelöscht wurde.")  # Custom error message
                return 

    # Wartet auf Benutzereingabe
    def get_input(self, prompt):
        return input(prompt)

    # Zielverzeichnis auswählen
    def move_and_rename(self, file_path):   
        # Wiederholen bis eine gültige Eingabe erkannt wird
        while True:
            dest_directory = self.get_input(f"Wählen Sie ein Zielverzeichnis:\n" +
                                            "\n".join([f"{key}: {path}" for key, path in self.directories.items()]) +
                                            "\nGeben Sie die Nummer des Verzeichnisses ein:  ")
            
            # Überprüfe ob die Eingabe gültig ist
            if dest_directory in self.directories:
                break  # Bricht while Loop ab
            else:
                print("Ungültige Eingabe. \nProbieren Sie es nochmals!")
        
        # Für dest_directory gilt das ausgewählte Zielverzeichnis
        new_directory = self.directories[dest_directory]
        
        if new_directory:
            while True:
                new_file_name = self.get_input("Neuen Dateinamen eingeben (ohne Erweiterung/Datentyp): ")
                
                if not new_file_name:
                    new_file_name = os.path.splitext(os.path.basename(file_path))[0]  # Behalte den aktuellen Name
                original_extension = os.path.splitext(file_path)[1]
                new_file_path = os.path.join(new_directory, f"{new_file_name}{original_extension}")
                
                # Kontrolliert ob im Zielverzeichnis schon eine Datei mit dem gleichen Name und Datentyp existiert
                if os.path.exists(new_file_path):
                    print(f"Im Zielverzeichnis gibt es bereits eine Datei mit diesem Namen.") 
                    print("Bitte wähle einen anderen Namen aus.")
                else:
                    # Verschiebe, falls möglich
                    try:
                        shutil.move(file_path, new_file_path)
                        print(f"Datei wurde erfolgreich verschoben und umbenannt. Ort: {new_file_path}")
                        break  
                    # Fehlerbehandlung
                    except FileNotFoundError:
                        print(f"Fehler: Die datei '{file_path}' kann ich nicht mehr finden.")
                        return  
                    except PermissionError:
                        print(f"Fehler: Zugriff verweigert. Sie haben keine Berechtigung, die Datei in das Verzeichnis '{new_directory}' zu verschieben.")
                        return  
                    except OSError as e:
                        print(f"Prozess fehlgeschlagen: {e}.")
                        return 
                    except Exception as e:
                     
                        print(f"Wie peinlich, irgendetwas ist fehlgeschlafen: {e}.")
                        return 
                    

if __name__ == "__main__":
    path_to_watch = get_download_folder()  # Findet Verzeichnispfad vom Download-Verzeichnis
    directories = load_directories()  # Importiert Verzeichnisse aus directories.txt
    event_handler = FileHandler(directories)
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=False)
    
    print(f"Ich überwache: {path_to_watch}")
    observer.start() # Started die überwachung
    
    try:
        while True:
            time.sleep(1) # Das ist um Resourcen zu sparen (CPU)
    except KeyboardInterrupt: # Fängt die Tastenkombination Strg+C ab, um das Script zu beenden
        print("Das Skript wurde abgebrochen. Bis zum nächsten mal <3")
        observer.stop() 
    observer.join() # Wartet, bis der Überwachungsprozess vollständig gestoppt ist, bevor das Programm endet.
