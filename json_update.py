import json
import os

FATAL = "[FATAL]\n"
def openFile(filename = ""):
    '''
        type filename: string
        rtype: dict or False
    '''
    try: 
        connection_file = open(filename, 'r')
        conn_string = json.load(connection_file)
        connection_file.close()
        return conn_string
    except IOError as e:
        wfile = open(filename,'w')
        wfile.write(json.dumps([]))
        wfile.close()
        with open(filename, 'r') as connection_file:
            conn_string = json.load(connection_file)
        return conn_string
    except Exception as e:
        # Catching exception error when loading the JSON file.
        file = filename.split("/")
        print(FATAL + '"%s" of %s.  Unable to read the file.'
              % (e.args[0],file[-1]))
        print(FATAL)
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

def json_update(data):
    util = open('job.json', 'r')
    re_util = json.load(util)
    
    re_util.append(data)
    util = open('job.json', 'w')
    util.write(json.dumps(re_util))
    util.close()

def displayJSON(jsonObject):
    '''
        type jsonObject: dict
        rtype: string
    '''
    return json.dumps(jsonObject, indent=4)
