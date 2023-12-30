import os
import sys
import glob
import time
import shutil
from datetime import datetime, timedelta
import customgpt_client
import schedule
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# Set up the API key and client
API_TOKEN = "YOUR_API_TOKEN"
client = customgpt_client.Client(API_TOKEN)

# Set up the project name, sitemap path, and watched folder
PROJECT_NAME = "your_project_name"
SITEMAP_PATH = "your_sitemap_path"
WATCHED_FOLDER = "your_watched_folder"

# Set the number of days after which files will be deleted
DELETE_AFTER_DAYS = 30

# Set up the CustomGPT project
project = client.get_project(PROJECT_NAME)
if not project:
    project = client.create_project(PROJECT_NAME, SITEMAP_PATH)

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        # Append the current date to the filename
        filename = f"{event.src_path}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Upload the file to the CustomGPT project
        with open(event.src_path, "rb") as f:
            client.source.create(project.id, filename, f)

        # Move the file to a processed folder
        processed_folder = os.path.join(WATCHED_FOLDER, "processed")
        os.makedirs(processed_folder, exist_ok=True)
        shutil.move(event.src_path, processed_folder)

# Set up the watchdog observer
observer = Observer()
observer.schedule(FileHandler(), WATCHED_FOLDER, recursive=False)
observer.start()

# Periodically delete old files
def delete_old_files():
    for file in glob.glob(f"{WATCHED_FOLDER}/*"):
        if os.path.isfile(file):
            file_age = datetime.now() - datetime.fromtimestamp(os.path.getctime(file))
            if file_age > timedelta(days=DELETE_AFTER_DAYS):
                os.remove(file)

# Schedule the file deletion task
schedule.every().day.at("00:00").do(delete_old_files)

# Run the script continuously
while True:
    schedule.run_pending()
    time.sleep(1)
