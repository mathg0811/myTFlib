# watch_pyx.py
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import subprocess
import time
import os


class PyxHandler(PatternMatchingEventHandler):
    def __init__(self):
        super().__init__(patterns=["*.pyx"], ignore_directories=True)

    def on_modified(self, event):
        print(f"Detected change in {event.src_path}, rebuilding...")
        subprocess.run(["python", "setup.py", "build_ext", "--inplace"])


if __name__ == "__main__":
    path = os.path.abspath("src")
    event_handler = PyxHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    print(f"Watching for .pyx changes in: {path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
