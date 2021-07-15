import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ChangeHandler(FileSystemEventHandler):

    # def on_deleted(self, event):
    #     src_name = os.path.basename(event.src_path)
    #     print(f'{src_name}を削除しました')

    # def on_created(self, event):
    #     # ファイル名取得
    #     src_name = os.path.basename(event.src_path)
    #     print(f'{src_name}ができました')
    pass


def watch_start(path):
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

watch_path = os.path.abspath(os.path.dirname(__file__))

watch_start(watch_path)