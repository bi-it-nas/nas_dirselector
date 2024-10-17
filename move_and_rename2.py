import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

# Function to get the download folder path based on the platform
def get_download_folder():
    return str(Path.home() / "Downloads")

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Ignores directories
        if event.is_directory:
            return
        
        file_path = event.src_path

        if os.path.splitext(file_path)[1] == ".tmp":
            print("Temp file detected, ignoring")
            return
        else:
            print(f"New file detected: {file_path}")

            # Proceed with processing the file (renaming/moving)
            try:
                self.move_and_rename(file_path)
            except FileNotFoundError:
                print("Something went wrong!")  # Custom error message
                return  # Proceed to keep monitoring new files

    # Function to get user input
    def get_input(self, prompt):
        return input(prompt)

    # Ask user for a destination directory
    def move_and_rename(self, file_path):   
        # Define valid directories
        directories = {
            '1': "C:\\Users\\sameu\\Documents",
            '2': "C:\\Users\\sameu\\Desktop",
            '3': "C:\\Users\\sameu\\Pictures"
        }
        
        # Keep asking until a valid input is given
        while True:
            dest_directory = self.get_input("Choose a destination directory:\n1: C:\\Users\\sameu\\Documents\n2: C:\\Users\\sameu\\Desktop\n3: C:\\Users\\sameu\\Pictures\nEnter the number of the directory: ")
            
            # Check if the input is valid
            if dest_directory in directories:
                break  # Exit loop if a valid input is given
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        
        # Now dest_directory holds the chosen valid directory path
        new_directory = directories[dest_directory]
        
        if new_directory:
            while True:
                new_file_name = self.get_input("Enter new file name (without extension): ")
                
                if not new_file_name:
                    new_file_name = os.path.splitext(os.path.basename(file_path))[0]  # Keep the original name if input is empty
                original_extension = os.path.splitext(file_path)[1]
                new_file_path = os.path.join(new_directory, f"{new_file_name}{original_extension}")
                
                # Check if file already exists in the new directory
                if os.path.exists(new_file_path):
                    print(f"A file with the name '{new_file_name}{original_extension}' already exists in the destination directory.")
                    print("Please choose a different name.")
                else:
                    # Move the file if no conflict
                    try:
                        shutil.move(file_path, new_file_path)
                        print(f"File moved and renamed to: {new_file_path}")
                        break  # Exit the loop once the file is successfully moved
                    except FileNotFoundError:
                        print("Something went wrong!")  # Handle file not found error
                        return  # Proceed to keep monitoring new files


if __name__ == "__main__":
    path_to_watch = get_download_folder()  # Dynamically get the Downloads folder path
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=False)
    
    print(f"Monitoring folder: {path_to_watch}")
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join() 
