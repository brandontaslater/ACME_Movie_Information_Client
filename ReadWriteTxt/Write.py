from pathlib import Path
import json
import re
from ReadWriteTxt import ReadFromTxt


def split_dict_key(data_dict):
    list_keys = list(data_dict.keys())
    keys = ""
    for each in list_keys:
        keys = keys + json.dumps(each) + "|"
    return (re.sub('["]', '', keys))[:-1]


def split_dict_value(data_dict):
    list_items = list(data_dict.values())
    items = ""
    for each in list_items:
        items = items + json.dumps(each) + "|"
    return (re.sub('["]', '', items))[:-1]


def write_dict(data_dict, path):
    print("Write")
    print(data_dict)
    key = split_dict_key(data_dict)
    value = split_dict_value(data_dict)

    if path.is_file():
        print("Hello")
        print(ReadFromTxt.get_record_number(path))
        print("Hello1")
        recordNo = int(ReadFromTxt.get_record_number(path))
        print(recordNo)
        print("Hello2")
        recordNo = recordNo + 1
        print("Hello3")
        file = open(path, "a")
        file.write("\n" + str(recordNo) + "|" + value)
        file.close()
    else:
        file = open(path, "w")
        file.write("RecordID|" + key)
        file.write("\n"+"1|" + value)
        file.close()
    print("Finished Write")
