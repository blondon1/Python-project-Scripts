from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import json
# pip install watchdog /or/ poetry add watchdog    (required)
# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

class Handler(FileSystemEventHandler):
    def __init__(self, watched_folder, destination_folder):
        self.watched_folder = watched_folder
        self.destination_folder = destination_folder

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

