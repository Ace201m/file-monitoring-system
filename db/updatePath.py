from db.names import Names
from os import path

pathFile = Names.PATHFILE


def updatePath(dir_path):
    if path.exists(dir_path) and path.isdir(dir_path):
        with open(pathFile, 'w') as f:
            f.write(dir_path + '\n')
    else:
        print("Directory path invalid")


def getPath():
    with open(pathFile, 'r') as f:
        dir_path = f.read(100).strip()
    return dir_path
