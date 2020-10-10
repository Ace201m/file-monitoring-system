from db.names import Names


def validate(old_file, new_file, action_type):
    if action_type == 'CREATED':
        if new_file[Names.DB_DATA_COLLECTION_OWNER] == new_file[Names.DB_DATA_COLLECTION_PARENT_OWNER]:
            if new_file[Names.DB_DATA_COLLECTION_CONFIG] == Names.DB_CONFIGS_FLAG[3] or \
                    new_file[Names.DB_DATA_COLLECTION_CONFIG] == Names.DB_CONFIGS_FLAG[4] or \
                    new_file[Names.DB_DATA_COLLECTION_CONFIG] == Names.DB_CONFIGS_FLAG[5] or \
                    new_file[Names.DB_DATA_COLLECTION_CONFIG] == Names.DB_CONFIGS_FLAG[1]:
                return False
            else:
                return True
        else:
            return False
    elif action_type == 'DELETED':
        if new_file[Names.DB_DATA_COLLECTION_PARENT_OWNER] == old_file[Names.DB_DATA_COLLECTION_OWNER]:
            if new_file[Names.DB_DATA_COLLECTION_CONFIG] == Names.DB_CONFIGS_FLAG[0] or \
                    new_file[Names.DB_DATA_COLLECTION_CONFIG] == Names.DB_CONFIGS_FLAG[1] or \
                    new_file[Names.DB_DATA_COLLECTION_CONFIG] == Names.DB_CONFIGS_FLAG[4]:
                return False
            else:
                return True
        else:
            return False
    elif action_type == 'MODIFIED':
        if new_file[Names.DB_DATA_COLLECTION_OWNER] == old_file[Names.DB_DATA_COLLECTION_OWNER]:
            if old_file[Names.DB_DATA_COLLECTION_CONFIG] == Names.DB_CONFIGS_FLAG[0] or \
                    old_file[Names.DB_DATA_COLLECTION_CONFIG] == Names.DB_CONFIGS_FLAG[1] or \
                    old_file[Names.DB_DATA_COLLECTION_CONFIG] == Names.DB_CONFIGS_FLAG[3]:
                if old_file[Names.DB_DATA_COLLECTION_SIGN] == new_file[Names.DB_DATA_COLLECTION_SIGN]:
                    return True
                else:
                    return False
            elif old_file[Names.DB_DATA_COLLECTION_CONFIG] == Names.DB_CONFIGS_FLAG[2] or \
                    old_file[Names.DB_DATA_COLLECTION_CONFIG] == Names.DB_CONFIGS_FLAG[4] or \
                    old_file[Names.DB_DATA_COLLECTION_CONFIG] == Names.DB_CONFIGS_FLAG[5]:
                return True
        else:
            return False
    else:
        raise Exception('how did we get here :|')
