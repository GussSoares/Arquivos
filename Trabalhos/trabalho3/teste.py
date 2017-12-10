import os
from collections import deque

def search_directory(text_box, initial_path):

    string = text_box.split(" ")

    list = deque()

    # os.popen(("pdftotext {} ").format(f))

    for path, dirs, files in os.walk(initial_path):
        for f in files:
            if len(string) > 1:

                if string[0].lower() in f.lower() and string[1].lower() in f.lower() and not (path+f in list):
                    list.appendleft(str(path+f))

                if string[0].lower() in f.lower() and not (path+f in list):
                    list.append(str(path+f))

                if string[1].lower() in f.lower() and not (path+f in list):
                    list.append(str(path+f))

            else:

                if (string[0].lower() in f.lower()) and not (path+f in list):
                    list.append(str(path+f))

    print(len(list))
    return list

for f in search_directory("deepin interface", "/home/gustavo/Desktop/"):
    print(f)
