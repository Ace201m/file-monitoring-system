import pyinotify as ntfy
import os


class EventHandler(ntfy.ProcessEvent):
    def process_IN_CREATE(self, event):
        print("Creating:", event.pathname)

    def process_IN_DELETE(self, event):
        print(os.path.exists(event.pathname))
        print(event)
        print("Removing:", event.pathname)

    def process_IN_MODIFY(self, event):
        print("Modifying:", event.pathname)


if __name__ == '__main__':
    wm = ntfy.WatchManager()
    mask = ntfy.IN_DELETE | ntfy.IN_CREATE | ntfy.IN_MODIFY
    handler = EventHandler()
    notifier = ntfy.Notifier(wm, handler)
    wm.add_watch('../demo_dir', mask, rec=True)
    # Loop forever and handle events.
    notifier.loop()


