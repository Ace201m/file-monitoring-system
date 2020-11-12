from db.dbhelper import Database
from db.names import Names
from db.secureDB import admin


class Action:

    def __init__(self, action_id=-1, action_data=None):
        self.data = dict()
        if action_id == -1:
            self.data = action_data
        else:
            database = Database()
            self.data = database.get(Names.DB_ACTION_COLLECTION, action_id)

    def isValid(self):
        return self.data[Names.DB_ACTION_COLLECTION_ISVALID]

    def getData(self):
        columns = Names.DB_ACTION_FIELDS
        data_list = []
        for col in range(len(columns)):
            data_list.append(self.data[col])
        return data_list
