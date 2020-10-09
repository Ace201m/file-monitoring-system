import os
from datetime import datetime

from watchdog.events import FileSystemEventHandler

from db.action import Action
from db.data import Data
from db.dbhelper import Database
from db.names import Names
from system.validator import validate


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
            Names.DB_ACTION_COLLECTION_TIME: datetime.now().ctime(),
            Names.DB_ACTION_COLLECTION_ISVALID: validate(new_file.getData(), new_file.getData(), 'CREATED')
        })
        database = Database()
        database.insert(Names.DB_DATA_COLLECTION, new_file.getData())
        database.insert(Names.DB_ACTION_COLLECTION, new_action.getData())
        print("FILE INSERTED")

    def on_moved(self, event):
        super().on_moved(event)  # TODO last thing to do

    def on_deleted(self, event):
        super().on_deleted(event)
        filepath = os.path.abspath(event.src_path)
        old_file = Data(data_id=filepath)
        new_file = Data(event=event, data_id=0)
        new_action = Action(action_data={
            Names.DB_ACTION_COLLECTION_BY: old_file.getUser(),
            Names.DB_ACTION_COLLECTION_PATH: old_file.getPath(),
            Names.DB_ACTION_COLLECTION_TYPE: 'DELETED',
            Names.DB_ACTION_COLLECTION_TIME: datetime.now().ctime(),
            Names.DB_ACTION_COLLECTION_ISVALID: validate(old_file.getData(), new_file.getData(), 'DELETED')
        })
        database = Database()
        database.delete(Names.DB_DATA_COLLECTION, old_file.getPath())
        database.insert(Names.DB_ACTION_COLLECTION, new_action.getData())
        if not new_action.getData()[Names.DB_ACTION_COLLECTION_ISVALID]:
            pass  # TODO undo action pending
        print("FILE DELETED")

    def on_modified(self, event):
        super().on_modified(event)

