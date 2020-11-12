import os
from pandas.core.frame import DataFrame
from db.names import Names
import pandas as pd
from db.secureDB import admin


class Database:
    def __init__(self):

        if not os.path.exists(Names.DB_HOME):
            os.mkdir(Names.DB_HOME)

        if not os.path.exists(Names.PATHFILE):
            with open(Names.PATHFILE, 'w') as f:
                f.write(os.path.expanduser('~'))
        self.data = os.path.join(Names.DB_HOME, Names.DB_DATA_COLLECTION)
        self.action = os.path.join(
            Names.DB_HOME, Names.DB_ACTION_COLLECTION)
        if not os.path.exists(self.data):
            with open(self.data, 'w'):
                pass
        if not os.path.exists(self.action):
            with open(self.action, 'w'):
                pass

    def _encrypt(self, data: DataFrame):
        return data.applymap(lambda x: admin.encrypt(str(x)))

    def _decrypt(self, data: DataFrame):
        return data.applymap(lambda x: admin.decrypt(str(x)))

    def _read_file(self, filename, header):
        file: DataFrame = pd.read_csv(
            filename, names=header)
        return self._decrypt(file)

    def _write_file(self, filename, data):
        data = self._encrypt(data)
        data.to_csv(filename, index=False, header=False)

    def insert(self, section, data):
        """
        Insert data into the dataset
        """
        data = pd.DataFrame([data])
        if section == Names.DB_DATA_COLLECTION:
            data.columns = Names.DB_DATA_FIELDS
            file = self._read_file(self.data, Names.DB_DATA_FIELDS)
            file = file.append(data)
            self._write_file(self.data, file)
        else:
            data.columns = Names.DB_ACTION_FIELDS
            file = self._read_file(self.action, Names.DB_ACTION_FIELDS)
            file = file.append(data)
            self._write_file(self.action, file)

    def delete(self, section, path):
        """
        Delete data in the database
        """
        if section == Names.DB_DATA_COLLECTION:
            file = self._read_file(self.data, Names.DB_DATA_FIELDS)
            file = file[file[Names.DB_DATA_FIELDS[Names.DB_DATA_COLLECTION_PATH]]
                        != admin.encrypt(path)]
            self._write_file(self.data, file)
        else:
            print("Action can't be deleted")
            quit()

    def list2dict(self, data_list):
        data_dict = {}
        data_list = list(data_list)
        for name, value in zip(range(len(data_list)), data_list):
            data_dict[name] = value
        return data_dict

    def get(self, section, path):
        """
        get one data point from the database
        """
        if section == Names.DB_DATA_COLLECTION:
            file = self._read_file(self.data, Names.DB_DATA_FIELDS)
            file = file[file[Names.DB_DATA_FIELDS[Names.DB_DATA_COLLECTION_PATH]]
                        == path]
            return self.list2dict(file.values[0])
        else:
            print("Single Action getter is not permitted")
            quit()

    def getAll(self, section):
        """
        Get all entries in the
        """
        if section == Names.DB_ACTION_COLLECTION:
            file = self._read_file(self.action, Names.DB_ACTION_FIELDS)
            dict_list = []
            for action in file.values:
                dict_list.append(self.list2dict(action))
            return dict_list
        else:
            print("All Data getter is not permitted")
            quit()
