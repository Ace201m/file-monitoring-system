from db.action import Action
import datetime
from db.names import Names

reportPath = 'report.txt'


def writeAction(f, action):
    actionTime = action[Names.DB_ACTION_COLLECTION_TIME]
    actionType = action[Names.DB_ACTION_COLLECTION_TYPE]
    filePath = action[Names.DB_ACTION_COLLECTION_PATH]
    userResponsible = action[Names.DB_ACTION_COLLECTION_BY]
    comment = """
\t Action Type : {}
\t Time : {}
\t Concerned File : {}
\t User Responsible : {}
""".format(actionType, actionTime, filePath, userResponsible)
    f.write(comment)


def getReport(db):
    with open(reportPath, 'a') as f:
        f.write('-'*40 + '\n')
        f.write("Report generated on {}\n".format(datetime.datetime.now().ctime()))
        actions = db.getAll(Names.DB_ACTION_COLLECTION)
        for action in actions:
            if action[Names.DB_ACTION_COLLECTION_ISVALID] == 'False':
                writeAction(f, Action(action_data=action).getData())

        f.write('\n' + '-' * 40 + '\n')
