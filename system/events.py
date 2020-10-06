from watchdog.events import FileSystemEventHandler


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()

    def on_created(self, event):
        super().on_created(event)

    def on_moved(self, event):
        super().on_moved(event)

    def on_deleted(self, event):
        super().on_deleted(event)

    def on_modified(self, event):
        super().on_modified(event)

