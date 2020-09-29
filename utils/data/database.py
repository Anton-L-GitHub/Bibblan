import json

""" Database module concerned with """

json_file = 'utils/data/lib_register.json'


def disk_get():
    """ Returns a list of all instances in db-file """
    with open(json_file, 'r') as file:
        return json.load(file)


def disk_save(list_of_dicts):
    """ Takes list of instances attributes in form of a py-dict and writes it to a json file """
    with open(json_file, 'w') as file:
        json.dump(list_of_dicts, file)
