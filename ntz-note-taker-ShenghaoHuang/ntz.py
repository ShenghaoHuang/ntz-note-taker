#!/usr/bin/env python3
import yaml
import os
import sys
import json

# main function
"""
Breaking the project down to steps
Creating commands:
1. [R]emember will save the current note in the current location. ie ntz.py r "text file name" "contents of text file"
2. [-C] Creates or appends to a category so Im assuming how this would work is ntz -c Shopping -> If shopping category
or folder? exists create the note there
3. [F]orget will delete the contents of the text file or should I delete the file itself?
4. [E]dit Not entirely sure how this will work, edit should be able to edit a file, maybe the command E will open the text file in notepad or something
5. Clear will wipe a text document to be nothing, I think I can just replace the current txt file with a brand new one but same name

"""


# print(f'Number of arguments: {len(sys.argv)}')
# test = [x for x in sys.argv]
# print(test[0])
# print(sys.argv)
# print(dict_file[1])
# print(yaml.dump(dict_file))

def load_yaml():
    with open(r'/Users/sheng/Projects/ntz-note-taker-ShenghaoHuang/test.yaml') as notes:
        data = yaml.full_load(notes)
        return data


def save_yaml(dict):
    with open(r'/Users/sheng/Projects/ntz-note-taker-ShenghaoHuang/test.yaml', 'w') as save:
        saved = yaml.dump(dict, save)


def remember(dict):
    if len(sys.argv) == 3 and sys.argv[1] == '-r':
        dict['General'].append(sys.argv[2])
    elif len(sys.argv) == 4 and sys.argv[1] == '-r':
        dict[sys.argv[2]] = sys.argv[3]


def create(dict):
    if len(sys.argv) == 3:
        if sys.argv[1] == '-c':
            dict[sys.argv[2]] = []
    elif len(sys.argv) == 4:
        if sys.argv[1] == '-c':
            dict[sys.argv[2]] == [sys.argv[5]]


def forget(dict):
    if sys.argv[1] == '-f':
        if dict.has_key(sys.argv[2]) == True:
            del dict[sys.argv[2]]
        elif dict.has_key(sys.argv[2]) == False:
            print("Category does not exist")


def edit(category, dict):
    if sys.argv[1] == '-e':
        if dict.has_key(category) == True:
            dict[category] = dict.pop(sys.argv)
        elif dict.has_key(category) == False:
            print("Category does not exist")


def main():
    file = load_yaml()
    if len(sys.argv) == 1:
        print(yaml.dump(file))
    elif sys.argv[1] == 'r':
        remember(file)
    elif sys.argv[1] == '-c':
        create(file)
    elif sys.argv[1] == '-f':
        forget(file)
    elif sys.argv[1] == '-e':
        edit(file)
    save_yaml(file)


main()
