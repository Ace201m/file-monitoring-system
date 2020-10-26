from time import sleep

from db.dbhelper import Database
from db.updatePath import updatePath, getPath
from system.eventHandler import Event
from system.report import getReport


def main():
    db = Database()
    dir_path = getPath()
    while True:
        option = input("""
        
Basic Tripwire model:
    1. Update model working path (current : {})
    2. Start service
    3. Generate Report
    4. Exit
Select option (1/2/3/4/5) : """.format(dir_path))
        if option == '1':
            dir_path = input('Enter the new Path for the system : ')
            updatePath(dir_path)
        elif option == '2':
            Event(dir_path).run()
        elif option == '3':
            getReport(db)
            print()
            print("Waiting for 10 secs", end='')
            for _ in range(10):
                sleep(1)
                print('.', end='')
            print()
        elif option == '4':
            break
        else:
            print("Unknown action ... Exiting... ")
            break


if __name__ == '__main__':
    main()
