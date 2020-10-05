from db.dbhelper import Database
from system.system_init import prompt, Tripwire


def main():
    db = Database()
    while True:
        option = input("""
        
Basic Tripwire model:
    1. Setting up the System
    2. Updating file
    3. Generate Report
    4. Exit
Select option (1/2/3/4) : """)
        if option == '1':
            path = prompt()
            system = Tripwire(path)
            # TODO setting up system
        elif option == '2':
            pass
            # TODO updating file
        elif option == '3':
            pass
            # TODO generating report
        else:
            print("Unknown action ... Exiting... ")
            break


if __name__ == '__main__':
    main()
