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
import hashlib
import datetime as dt
class Backend():

    



    
    def hash_dest(dir: str) -> dict[str, None]:
        files = ["%s/%s" % (dir, i) for i in os.listdir(dir) if os.path.isfile(i)]
        hashes = {}
        for i in files:
            with open(i, "rb") as bin:
                contents = bin.read()
                sha = hashlib.sha256()
                sha.update(contents)
                hashes[sha.hexdigest()] = None

        return hashes

    
    def hash_src(dir: str) -> tuple[dict[str, tuple[str, bytes]], list]:
        files = ["%s/%s" % (dir, i) for i in os.listdir(dir) if os.path.isfile("%s/%s" % (dir, i))]
        hash_list = []
        m = {}

        for i in files:
            with open(i, "rb") as bin:
                contents = bin.read()
                sha = hashlib.sha256()
                sha.update(contents)
                hash_list.append(sha.hexdigest())
                m[sha.hexdigest()] = (i, contents)
        return m, hash_list

    def cross_check(src_list: list, src_map: dict[str, tuple[str, bytes]], dest_map: dict[str, None], dest: str, output: QTextEdit) -> None:
        for i in src_list:
            try:
                check = dest_map[i]
            except:
                file_name = src_map[i][0].split("/")[-1]
                contents = src_map[i][1]
                path = "%s/%s" % (dest, file_name)
                #output.append("Writing %s to destination." % file_name)
                print("Writing %s to destination." % file_name)
                with open(path, "wb") as bin:
                    bin.write(contents)
                #output.append("%s done.\n" % file_name)
                print("%s done.\n" % file_name)
            else:
                pass

    def run(src: str, dest: str, output: QTextEdit) -> None:
        dest_dict = Backend.hash_dest(dest)
        src_dict, src_list = Backend.hash_src(src)

        Backend.cross_check(src_list, src_dict, dest_dict, dest, output)


class GUI():


    def __init__(self):
        self.view = QMainWindow()
        self.view.setWindowTitle("Python Bulk File Transfer")
        self.view.setFixedHeight(800)
        self.view.setFixedWidth(800)
        self._main_view = self.main_view()
        self._search_view = None
        self.model = None


    def show_main(self) -> None:
        self.view.setCentralWidget(self._main_view)
        self.view.show()

    def show_search(self) -> None:
        self.view.setCentralWidget(self._search_view)

    
    def run_backend(self, dir_one: QLineEdit, dir_two: QLineEdit, output: QTextEdit) -> None:
        src = dir_one.text()
        dest = dir_two.text()


        Backend.run(src, dest, output)



    def main_view(self) -> QWidget:
        widget = QWidget()
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        dir_one = QLineEdit()
        dir_one.setFixedWidth(300)
        dir_one_b = QPushButton("Search")


        dir_two = QLineEdit()
        dir_two.setFixedWidth(300)
        dir_two_b = QPushButton("Search")

        dir_one_l = QLabel("Source Directory:")
        dir_two_l = QLabel("Destination Directory:")

        dir_one_b.clicked.connect(lambda: self.choose_file(dir_one))
        dir_two_b.clicked.connect(lambda: self.choose_file(dir_two))


        layout.addWidget(dir_one_l, 0, 0, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(dir_one, 0, 1, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(dir_one_b, 0, 2, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        layout.addWidget(dir_two_l, 1, 0, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(dir_two, 1, 1, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(dir_two_b, 1, 2, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)




        output = QTextEdit()
        output.setReadOnly(True)
        layout.addWidget(output, 3, 1, Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)


        src = dir_one.text()
        dest = dir_two.text()

        transfer = QPushButton("Transfer")
        transfer.clicked.connect(lambda: self.run_backend(dir_one, dir_two, output))
        layout.addWidget(transfer, 2, 1, Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop )



        widget.setLayout(layout)

        return widget
        

    def choose_file(self, line: QLineEdit) -> None:
        line.setText(QFileDialog.getExistingDirectoryUrl().path().removeprefix("/"))











