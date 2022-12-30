import hashlib
import hashlib as hl
import sys
import pathlib as path
import os
import io


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
    for i in dest.keys():
        try:
            check = source[i]
        except:
            pass


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
    '''
    dirs = choose_dirs()
    source = dirs[0]
    dest = dirs[1]
    '''


    source = "C:/Users/desmo/projects/FileTransfer"
    dest = "C:/Users/desmo/projects/FileTransfer/testing"
    

    s = get_file_names(source)
    d = get_file_names(dest)
    s_f = get_bytes_source(s)
    d_f = get_bytes_dest(d)
    
    print(s_f)
    print(d_f)






if __name__ == "__main__":
    main()

