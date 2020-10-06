from db.names import Names
import os
from pathlib import Path


def prompt():
    while True:
        option = input("""
Select a flag for a new file created : 
    1. READ ONLY
    2. FULL SCAN
    3. NO SCAN
    4. SYSTEM FILE
    5. EXECUTABLE
    6. HIDDEN_FILE
Select your option : """)
        try:
            return Names.DB_CONFIGS_FLAG[int(option) - 1]
        except ValueError:
            print("Unexpected option, Try again")


class Data:
    def __init__(self, data_id=-1, event=None):
        if data_id == -1:
            self.data = dict()
            filepath = os.path.abspath(event.src_path)
            fileInfo = Path(filepath)
            self.data[Names.DB_DATA_COLLECTION_PATH] = filepath
            self.data[Names.DB_DATA_COLLECTION_SIGN] = 'SIGN'

            self.data[Names.DB_DATA_COLLECTION_CONFIG] = prompt()
            self.data[Names.DB_DATA_COLLECTION_TYPE] = 'DIR' if event.is_directory else 'FILE'
            self.data[Names.DB_DATA_COLLECTION_OWNER] = fileInfo.owner()
            self.data[Names.DB_DATA_COLLECTION_PARENT_OWNER] = str(fileInfo.parent)
        else:
            pass
            # TODO getting file from database

    def getPath(self):
        return self.data[Names.DB_DATA_COLLECTION_PATH]

    def getUser(self):
        return self.data[Names.DB_DATA_COLLECTION_OWNER]

    def getData(self):
        return self.data
