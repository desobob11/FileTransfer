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


        transfer = QPushButton("Transfer")
        layout.addWidget(transfer, 2, 1, Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop )


        output = QTextEdit()
        output.setReadOnly(True)
        layout.addWidget(output, 3, 1, Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

        widget.setLayout(layout)

        return widget
        

    def choose_file(self, line: QLineEdit) -> None:
        line.setText(QFileDialog.getExistingDirectoryUrl().path().removeprefix("/"))











