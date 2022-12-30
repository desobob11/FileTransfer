import hashlib
import hashlib as hl
import sys
import pathlib as path
import os
import io


def get_file_names(dir:str) -> None:
    return [i for i in os.listdir(dir) if os.path.isfile(i)]


def get_bytes (files:list) -> dict:
    binary = {}


    for i in files:
        with open(i, "rb") as file:
            b = file.read()
            h1 = hl.sha256()
            h1.update(b)
            pair = (b,i)



            binary[h1.hexdigest()] = pair
    return binary






    ''' file_path = "%s/%s" % (str, i) '''








    with open("file.txt", "rb") as file:
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
    l = get_file_names(os.getcwd())
    m = get_bytes(l)
    print(m)




if __name__ == "__main__":
    main()