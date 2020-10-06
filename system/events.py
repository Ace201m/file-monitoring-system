from datetime import datetime

from watchdog.events import FileSystemEventHandler

from db.action import Action
from db.data import Data
from db.dbhelper import Database
from db.names import Names


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()

    def on_created(self, event):
        super().on_created(event)
        new_file = Data(event=event)
        new_action = Action(action_data={
            Names.DB_ACTION_COLLECTION_BY: new_file.getUser(),
            Names.DB_ACTION_COLLECTION_PATH: new_file.getPath(),
            Names.DB_ACTION_COLLECTION_TYPE: 'CREATED',
            Names.DB_ACTION_COLLECTION_TIME: datetime.now().ctime()
        })
        database = Database()
        database.insert(Names.DB_DATA_COLLECTION, new_file.getData())
        database.insert(Names.DB_ACTION_COLLECTION, new_action.getData())
        print("FILE INSERTED")

    def on_moved(self, event):
        super().on_moved(event)

    def on_deleted(self, event):
        super().on_deleted(event)

    def on_modified(self, event):
        super().on_modified(event)

