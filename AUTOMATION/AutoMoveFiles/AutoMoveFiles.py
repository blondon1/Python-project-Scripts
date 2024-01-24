from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# pip install watchdog /or/ poetry add watchdog    (required)

import time
import os
import json

class Handler(FileSystemEventHandler):
    def __init__(self, watched_folder, destination_folder):
        self.watched_folder = watched_folder
        self.destination_folder = destination_folder

    def on_modified(self, event):
        if not event.is_directory:
            # List only files to avoid moving directories
            files = [f for f in os.listdir(self.watched_folder) if os.path.isfile(os.path.join(self.watched_folder, f))]
            for file in files:
                src = os.path.join(self.watched_folder, file)
                dst = os.path.join(self.destination_folder, file)
                if not os.path.exists(dst):
                    os.rename(src, dst)
                    logging.info(f"Moved: {src} -> {dst}")
                else:
                    # Handle duplicate files by appending an index
                    base, extension = os.path.splitext(dst)
                    counter = 1
                    new_dst = f"{base}_{counter}{extension}"
                    while os.path.exists(new_dst):
                        counter += 1
                        new_dst = f"{base}_{counter}{extension}"
                    os.rename(src, new_dst)
                    logging.info(f"Moved: {src} -> {new_dst}")

if __name__=="__main__":
    watched_folder = input("Paste the path to the folder to be tracked: ")
    destination_folder = input("Paste the path to the destination folder: ")
    handler = Handler()
    observer = Observer()
    observer.schedule(event_handler=handler, path=watched_folder, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

