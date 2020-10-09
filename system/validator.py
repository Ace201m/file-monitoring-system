from db.names import Names


def validate(old_file, new_file, action_type):
    if action_type == 'CREATED':
        if new_file[Names.DB_DATA_COLLECTION_OWNER] == new_file[Names.DB_DATA_COLLECTION_PARENT_OWNER]:
            return True
        else:
            return False
    elif action_type == 'DELETED':
        if new_file[Names.DB_DATA_COLLECTION_PARENT_OWNER] == old_file[Names.DB_DATA_COLLECTION_OWNER]:
            return True
        else:
            return False
    elif action_type == 'UPDATED':
        pass  # TODO pending
    else:
        raise Exception('how did we get here :|')
