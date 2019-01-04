import json
import os
import config

FATAL = "[FATAL]\n"
def _openFile(filename = ""):
    '''
        type filename: string
        rtype: dict or False
    '''
    try:
        if checkFileExist(filename):
            connection_file = open(filename, 'r')
            conn_string = json.load(connection_file)
            connection_file.close()
            return conn_string
        else:
            return False
    except Exception as e:
        # Catching exception error when loading the JSON file.
        file = filename.split("/")
        print(FATAL + '"%s" of %s.  Unable to read the file.'
              % (e.args[0],file[-1]))
        print(FATAL)

def parseDirectory(path = config.TEST_CASE_FOLDER_PATH):
    files = []
    for i in os.listdir(path):
        if i.endswith('.json'):
            files.append(i)
    return files
def checkFileExist(filename = "",print_message = True):
    '''
        type filename: string
        type print_message: boolean
        rtype: True or False
    '''
    if os.path.isfile(filename):
        return True
    else:
        if print_message:
            # Throw an error message stating the file doesn't exist
            fname = filename.split("/")
            print("[%s] does not exist." % fname[-1])
        return False
def removeFile(filename = ""):
    '''
        type filename: string
    '''
    os.remove(filename)

def displayJSON(jsonObject):
    '''
        type jsonObject: dict
        rtype: string
    '''
    return json.dumps(jsonObject)

def parseJSON(filename = ""):
    '''
        type filename: string
        rtype: dictionay
    '''
    name_json = ".json"
    filename = filename + name_json
    conn_string = _openFile(config.TEST_CASE_FOLDER_PATH + filename)
    if conn_string:
        return conn_string
    else:
        print("Empty items in %s." % filename)






