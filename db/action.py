from db.names import Names


class Action:

    def __init__(self, action_id=-1, action_data=None):
        self.data = dict()
        if action_id == -1:
            self.data = action_data
        else:
            pass
            # TODO getting actions from the database

    def isValid(self):
        return self.data[Names.DB_ACTION_COLLECTION_ISVALID]

    def getData(self):
        return self.data
