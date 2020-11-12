import os
from pandas.core.frame import DataFrame
from db.names import Names
import pandas as pd


class Database:
    def __init__(self):

        if not os.path.exists(Names.DB_HOME):
            os.mkdir(Names.DB_HOME)

        if not os.path.exists(Names.PATHFILE):
            with open(Names.PATHFILE, 'w') as f:
                f.write(os.path.abspath('~'))
        self.data = os.path.join(Names.DB_HOME, Names.DB_DATA_COLLECTION)
        self.action = os.path.join(
            Names.DB_HOME, Names.DB_ACTION_COLLECTION)
        if not os.path.exists(self.data):
            with open(self.data, 'w'):
                pass
        if not os.path.exists(self.action):
            with open(self.action):
                pass

    def insert(self, section, data):
        """
        Insert data into the dataset
        """
        if section == Names.DB_DATA_COLLECTION:
            file: DataFrame = pd.read_csv(
                self.data, header=Names.DB_DATA_FIELDS)
            file = file.append(data)
            file.to_csv(self.data)
        else:
            file: DataFrame = pd.read_csv(
                self.action, header=Names.DB_ACTION_FIELDS)
            file = file.append(data)
            file.to_csv(self.data)

    def delete(self, section, path):
        """
        Delete data in the database
        """
        if section == Names.DB_DATA_COLLECTION:
            file: DataFrame = pd.read_csv(
                self.data, header=Names.DB_DATA_FIELDS)
            file = file[Names.DB_DATA_COLLECTION_PATH != path]
            file.to_csv(self.data)
        else:
            print("Action can't be deleted")
            quit()

    def list2dict(self, cols, data_list):
        data_dict = {}
        for name, value in zip(cols, data_list):
            data_dict[name] = value
        return data_dict

    def get(self, section, path):
        """
        get one data point from the database
        """
        if section == Names.DB_DATA_COLLECTION:
            file: DataFrame = pd.read_csv(
                self.data, header=Names.DB_DATA_FIELDS)
            file = file[Names.DB_DATA_COLLECTION_PATH == path]
            return self.list2dict(Names.DB_DATA_FIELDS, file)
        else:
            print("Single Action getter is not permitted")
            quit()
