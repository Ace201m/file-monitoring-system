import os


def prompt():
    path = input("""Enter Directory path for monitoring: """)

    if os.path.exists(path):
        return path
    else:
        raise Exception("Path entered is not valid")


class Tripwire:
    def __init__(self, path):
        with os.scandir(path) as dir_contents:
            for entry in dir_contents:
                info = entry.stat()
                print(info)
