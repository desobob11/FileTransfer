import hashlib
import hashlib as hl
import sys
import pathlib as path
import os
import io

from PyQt6.QtWidgets import *
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QStandardItemModel
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
import pathlib
import sys
import os
import pickle
import sqlalchemy as sql
from GUI import GUI

def get_file_names(dir:str) -> None:
    return [i for i in os.listdir(dir) if os.path.isfile(i)]


def get_bytes_source(files:list) -> dict:
    binary = {}

    for i in files:
        with open(i, "rb") as file:
            b = file.read()
            h1 = hl.sha256()
            h1.update(b)
            pair = (b,i)

            binary[h1.hexdigest()] = pair
    return binary



def get_bytes_dest(files: list) -> dict:
    binary = {}

    for i in files:
        with open(i, "rb") as file:
            b = file.read()
            h1 = hl.sha256()
            h1.update(b)
            binary[h1.hexdigest()] = file
    return binary

'''
    source_dict = dict(hash : [data, file name])
    dest_dict = dict(hash : file_name)

'''


def cross_check(source: dict, dest: dict, source_dir: str, dest_dir: str) -> dict:

    for i in source.keys():
        try:
            check = dest[i]
        except:
            source_i = source[i]
            with open(source_i[1], "wb") as file:
                with open("%s/%s" % (dest_dir, dest[1]), "wb") as bin:
                    bin.write(file.read())



            


'''
    io.BytesIO()
    bytesarray()
    os.listdir()
    os.path.isfile()
    
    List Comp:
    l = [1,2,3,4,5,6]
    l = [i for i in l if i % 2 == 0]
'''


def choose_dirs() -> None:
    source = str(input("Source directory:\n"))
    destination = str(input("Destination directory"))
    return (source, destination)







def main():
    app = QApplication(sys.argv)

    gui = GUI()


    gui.show_main()






    app.exec()



if __name__ == "__main__":
    main()

