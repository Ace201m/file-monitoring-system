import os
from os import name, system
from time import sleep

from db.dbhelper import Database
from db.updatePath import updatePath, getPath
from system.eventHandler import Event
from system.report import getReport


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main():

    if os.geteuid() != 0:
        exit("""You need to have root privileges to run this project.
Please try again, this time using 'sudo' or use admin cmd in windows. Exiting.""")

    db = Database()
    dir_path = getPath()
    while True:
        clear()
        option = input("""
File Monitoring System:
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
            print('Report is added to the report.txt file present in the project root')
            sleep(3)
        elif option == '4':
            break
        else:
            print("Unknown action ... Try Again... ")
            sleep(2)


if __name__ == '__main__':
    main()
