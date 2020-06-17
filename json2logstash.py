import fnmatch
import json
import os
from pathlib import Path


def get_data_from_json(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data


def get_filename_from_json(json_object):
    filenames_from_json = list()
    for data in json_object["values"]:
        filenames_from_json.append(data["id"] + "-" + data["name"] + ".conf")
    return filenames_from_json


def get_filenames_from_dir(dir_path):
    return fnmatch.filter(os.listdir(dir_path), "*.conf")


def get_lists_diff(list_json, list_dir):
    return list(set(list_json) - set(list_dir))


def read_data_from_file(file_path, zone):
    file_in = open(file_path, "rt")
    return file_in


def main():
    data_from_json = get_data_from_json(Path("logstash.json"))
    filenames_from_json = get_filename_from_json(data_from_json)
    filenames_from_dir = get_filenames_from_dir("/Users/test/Desktop/Test")

    print("Values from JSON:\n" + str(filenames_from_json))
    print("Values from dir:\n" + str(filenames_from_dir))
    print("Difference between:\n" + str(get_lists_diff(filenames_from_json, filenames_from_dir)))
    print("File contents:\n" + str(read_data_from_file("template.conf", "prod")))


if __name__ == '__main__':
    main()
