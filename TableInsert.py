from PyQt5.QtGui import QTextTableFormat, QColor, QTextTable, QTextTableCell
from PyQt5.QtWidgets import QDialog, QLabel, QSpinBox, QGridLayout, QPushButton, QColorDialog


class TableInsert(QDialog):
    def __init__(self, TextEdit):
        QDialog.__init__(self, TextEdit)
        self.setWindowTitle("Insert table")
        self.setBaseSize(300, 300)
        self.TextEdit = TextEdit

        columns_label = QLabel("Columns: ", self)
        self.columns = QSpinBox(self)
        self.columns.setMinimum(1)

        rows_label = QLabel("Rows: ", self)
        self.rows = QSpinBox(self)
        self.rows.setMinimum(1)

        cell_spacing_label = QLabel("Cell spacing: ", self)
        self.cell_spacing = QSpinBox(self)
        self.cell_spacing.setValue(5)
        self.cell_spacing.setMinimum(1)

        cell_padding_label = QLabel("Cell padding: ", self)
        self.cell_padding = QSpinBox(self)
        self.cell_padding.setValue(5)
        self.cell_padding.setMinimum(1)

        self.color_label = QLabel("Background color", self)
        self.background_color = QColorDialog()
        self.color = self.background_color.currentColor()
        self.color_button = QPushButton()
        self.color_button.setToolTip("Background color")
        self.color_button.clicked.connect(lambda: self.set_background_color(self.color_button,
                                                                            self.background_color))

        self.insert_button = QPushButton("Insert", self)
        self.insert_button.clicked.connect(self.insert_action)
        self.insert_button.setShortcut("Enter")

        self.layout = QGridLayout()

        self.layout.addWidget(columns_label, 0, 0)
        self.layout.addWidget(self.columns, 0, 1)

        self.layout.addWidget(rows_label, 1, 0)
        self.layout.addWidget(self.rows, 1, 1)

        self.layout.addWidget(cell_spacing_label, 2, 0)
        self.layout.addWidget(self.cell_spacing, 2, 1)

        self.layout.addWidget(cell_padding_label, 3, 0)
        self.layout.addWidget(self.cell_padding, 3, 1)

        self.layout.addWidget(self.color_label, 4, 0)
        self.layout.addWidget(self.color_button, 4, 1)

        self.layout.addWidget(self.insert_button, 5, 1)

        self.setLayout(self.layout)

    def insert_action(self):
        columns = self.columns.value()
        rows = self.rows.value()

        table_format = QTextTableFormat()
        table_format.setAlignment(self.TextEdit.alignment())
        table_format.setCellSpacing(self.cell_spacing.value())
        table_format.setCellPadding(self.cell_padding.value())
        table_format.setBackground(self.color)
        cursor = self.TextEdit.textCursor()
        cursor.insertTable(rows, columns, table_format)
        self.close()

    def set_background_color(self, color_button, color_dialog):
        self.color = QColor(color_dialog.getColor())
        color_button.setStyleSheet("background-color:" + self.color.name())
