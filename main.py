import sys
import json
from script import insert_data


def main():
    """
    The function reads json from a file and uploads it to the database after printing it.
    """
    data_list = []
    with open('source.json') as f:
        for json_obj in f:
            data_dict = json.loads(json_obj)
            data_list.append(data_dict)

    for data in data_list:
        insert_data(str(data))
        sys.stdout.write(str(data))
        sys.stdout.write('\n')
