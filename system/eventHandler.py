import time

from watchdog.observers import Observer
from system.events import FileEventHandler


class Event:
    def __init__(self, src_path_sys):
        self.__src_path = src_path_sys
        self.__event_handler = FileEventHandler()
        self.__event_observer = Observer()

    def run(self):
        self.start()
        print("Service is started (press Ctrl-C to stop)")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler,
            self.__src_path,
            recursive=True
        )


if __name__ == "__main__":
    Event('../demo_dir/').start()
