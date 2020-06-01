from PyQt5.QtCore import QSize
from PyQt5.QtGui import QTextTableFormat, QColor, QIcon, QTextListFormat
from PyQt5.QtWidgets import QDialog, QLabel, QSpinBox, QGridLayout, QPushButton, QColorDialog

class List(QDialog):
    def __init__(self, TextEdit):
        QDialog.__init__(self, TextEdit)
        self.editor = TextEdit
        self.setWindowTitle("Select list form")
        # self.setMinimumSize(700, 300)
        self.layout = QGridLayout()

        number_button = QPushButton()
        number_button.setIconSize(QSize(32, 32))
        number_button.setIcon(QIcon("icons/numbered-list.png"))
        number_button.setToolTip("Decimal values in ascending order")
        number_button.clicked.connect(lambda: self.number())

        #disc button
        disk_button = QPushButton()
        disk_button.setIconSize(QSize(32, 32))
        disk_button.setIcon(QIcon("icons/disk-list.png"))
        disk_button.setToolTip("A filled circle list")
        disk_button.clicked.connect(lambda: self.disk())

        #circle button
        circle_button = QPushButton()
        circle_button.setIconSize(QSize(32, 32))
        circle_button.setIcon(QIcon("icons/circle-list.png"))
        circle_button.setToolTip("An empty circle list")
        circle_button.clicked.connect(lambda: self.circle())
        
        #square button
        square_button = QPushButton()
        square_button.setIconSize(QSize(32, 32))
        square_button.setIcon(QIcon("icons/square-list.png"))
        square_button.setToolTip("An filled square list")
        square_button.clicked.connect(lambda: self.square())

        #def roman
        roman_button = QPushButton()
        roman_button.setIconSize(QSize(32, 32))
        roman_button.setIcon(QIcon("icons/list-roman-style-numbers.png"))
        roman_button.setToolTip("Upper roman numerals")
        roman_button.clicked.connect(lambda: self.roman())

        # Latin characters in alphabetical order
        latin_button = QPushButton()
        latin_button.setIconSize(QSize(32, 32))
        latin_button.setIcon(QIcon("icons/upper_latin.png"))
        latin_button.setToolTip("Upper latin characters in alphabetical order")
        latin_button.clicked.connect(lambda: self.latin())

        # lower roman
        lower_roman_button = QPushButton()
        lower_roman_button.setIconSize(QSize(32, 32))
        lower_roman_button.setIcon(QIcon("icons/roman-list.png"))
        lower_roman_button.setToolTip("Lower roman numerals")
        lower_roman_button.clicked.connect(lambda: self.lower_roman())

        lower_latin_button = QPushButton()
        lower_latin_button.setIconSize(QSize(32, 32))
        lower_latin_button.setIcon(QIcon("icons/lower_latin.png"))
        lower_latin_button.setToolTip("Lower latin characters in alphabetical order")
        lower_latin_button.clicked.connect(lambda: self.lower_latin())

        self.layout.addWidget(number_button, 1, 0)
        self.layout.addWidget(disk_button, 0, 1)
        self.layout.addWidget(circle_button, 0, 0)
        self.layout.addWidget(square_button, 1, 1)
        self.layout.addWidget(latin_button, 2, 0)
        self.layout.addWidget(roman_button, 2, 1)
        self.layout.addWidget(lower_roman_button, 3, 1)
        self.layout.addWidget(lower_latin_button, 3, 0)
        self.setMinimumSize(250, 128)
        self.setLayout(self.layout)


    def number(self):
        cursor = self.editor.textCursor()
        cursor.insertList(QTextListFormat.ListDecimal)
        self.close()

    def disk(self):
        cursor = self.editor.textCursor()
        cursor.insertList(QTextListFormat.ListDisc)
        self.close()

    def circle(self):
        cursor = self.editor.textCursor()
        cursor.insertList(QTextListFormat.ListCircle)
        self.close()

    def square(self):
        cursor = self.editor.textCursor()
        cursor.insertList(QTextListFormat.ListSquare)
        self.close()

    def roman(self):
        cursor = self.editor.textCursor()
        cursor.insertList(QTextListFormat.ListUpperRoman)
        self.close()


    def lower_roman(self):
        cursor = self.editor.textCursor()
        cursor.insertList(QTextListFormat.ListLowerRoman)
        self.close()

    def latin(self):
        cursor = self.editor.textCursor()
        cursor.insertList(QTextListFormat.ListUpperAlpha)
        self.close()

    def lower_latin(self):
        cursor = self.editor.textCursor()
        cursor.insertList(QTextListFormat.ListLowerAlpha)
        self.close()