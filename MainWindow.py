from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QFileInfo
from PyQt5.QtGui import QColor, QIcon, QKeySequence, QImage, QTextTable, QTextTableFormat
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtWidgets import *

from List import List
from TableInsert import TableInsert
from TextEdit import *


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.editor = TextEdit()
        self.setCentralWidget(self.editor)

        self.path = ""
        self.file_name = ""

        self.menubar = self.menuBar()

        self.init_file_menu()  # File menu
        self.init_edit_menu()  # Edit menu
        self.init_font_menu()   # Font menu
        self.init_align_menu()  # Align menu
        self.init_insert_menu()  # Insert menu

        self.editor.currentCharFormatChanged.connect(lambda: self.current_format_changed())
        self.editor.cursorPositionChanged.connect(lambda: self.cursor_position_changed())

    def init_file_menu(self):
        file_menu = self.menubar.addMenu("&File")

        new_file_action = file_menu.addAction(QIcon("icons/new.png"), "New file", lambda: self.new_file_event(),
                                              QKeySequence.New)

        open_file_action = file_menu.addAction(QIcon("icons/open.png"), "Open file", lambda: self.open_text_file(),
                                               QKeySequence.Open)

        save_file = file_menu.addAction(QIcon("icons/save.png"), "Save file", lambda: self.save_file(),
                                        QKeySequence.Save)

        save_file_as = file_menu.addAction(QIcon("icons/save_as.png"), "Save as..", lambda: self.save_file_as(),
                                           QtCore.Qt.CTRL + QtCore.Qt.ALT + QtCore.Qt.Key_S)

        file_menu.addSeparator()

        print_file = file_menu.addAction(QIcon("icons/print.png"), "Print", lambda: self.print(),
                                         QKeySequence.Print)

        print_preview = file_menu.addAction(QIcon("icons/preview.png"), "Print preview", lambda: self.preview(),
                                            QtCore.Qt.CTRL + QtCore.Qt.Key_K)

        export_pdf = file_menu.addAction(QIcon("icons/pdf.png"), "Export PDF", lambda: self.export_to_pdf())

        file_menu.addSeparator()

        close = file_menu.addAction(QIcon("icons/close.png"), "Close", lambda: self.close(),
                                    QKeySequence.Close)

        self.filebar = QToolBar()

        self.addToolBar(self.filebar)
        self.filebar.addAction(new_file_action)
        self.filebar.addAction(open_file_action)
        self.filebar.addAction(save_file)
        self.filebar.addAction(save_file_as)
        self.filebar.addSeparator()
        self.filebar.addAction(print_file)
        self.filebar.addAction(print_preview)
        self.filebar.addAction(export_pdf)

    def init_edit_menu(self):
        self.edit_menu = self.menubar.addMenu("&Edit")
        undo = self.edit_menu.addAction(QIcon("icons/undo.png"), "Undo", lambda: self.editor.undo(), QKeySequence.Undo)
        redo = self.edit_menu.addAction(QIcon("icons/redo.png"), "Redo", lambda: self.editor.redo(), QKeySequence.Redo)
        copy = self.edit_menu.addAction(QIcon("icons/copy.png"), "Copy", lambda: self.editor.copy(), QKeySequence.Copy)
        paste = self.edit_menu.addAction(QIcon("icons/paste.png"), "Paste", lambda: self.editor.paste(),
                                         QKeySequence.Paste)
        cut = self.edit_menu.addAction(QIcon("icons/cut.png"), "Cut", lambda: self.editor.cut(), QKeySequence.Cut)

        self.filebar.addSeparator()
        self.filebar.addAction(undo)
        self.filebar.addAction(redo)
        self.filebar.addAction(copy)
        self.filebar.addAction(paste)
        self.filebar.addAction(cut)

    def init_font_menu(self):

        self.font_menu = self.menubar.addMenu("&Font")
        self.font_dialog = QFontDialog()
        self.font_menu.addAction(QIcon("icons/font.png"), "Change font format", lambda: self.font_format())

        self.fontbar = QToolBar()
        self.addToolBar(self.fontbar)
        self.fonts = QFontComboBox()
        self.fonts.setCurrentFont(self.editor.font())
        self.fonts.currentFontChanged.connect(lambda: self.editor.setCurrentFont(self.fonts.currentFont()))
        self.fontbar.addWidget(self.fonts)
        self.font_size(self.fontbar)
        self.color_dialog = QColorDialog()
        self.color_button = QPushButton()
        self.color_button.setToolTip("Font color")

        self.fontbar.addAction(QIcon("icons/font-color.png"), "Font color",
                               lambda: self.font_color(self.color_button, self.color_dialog))
        self.fontbar.addWidget(self.color_button)

        self.fontbar.addSeparator()

        self.bold = self.fontbar.addAction(QIcon("icons/bold.png"), "Bold", self.bold)
        self.bold.setShortcut(QKeySequence.Bold)

        self.italic = self.fontbar.addAction(QIcon("icons/italic.png"), "Italic", self.italic)
        self.italic.setShortcut(QKeySequence.Italic)

        self.underline = self.fontbar.addAction(QIcon("icons/underline.png"), "Underline", self.underline)
        self.underline.setShortcut(QKeySequence.Italic)

        self.bold.setCheckable(True)
        self.italic.setCheckable(True)
        self.underline.setCheckable(True)

    def init_align_menu(self):
        align_menu = self.menubar.addMenu("&Align")

        self.left = align_menu.addAction(QIcon("icons/align-left.png"), "Left",
                                         lambda: self.editor.setAlignment(Qt.AlignLeft), QKeySequence("Ctrl+L"))

        self.center = align_menu.addAction(QIcon("icons/align-center.png"), "Center",
                                           lambda: self.editor.setAlignment(Qt.AlignCenter), QKeySequence("Ctrl+E"))

        self.right = align_menu.addAction(QIcon("icons/align-right.png"), "Right",
                                          lambda: self.editor.setAlignment(Qt.AlignRight), QKeySequence("Ctrl+R"))

        self.justify = align_menu.addAction(QIcon("icons/align-justify.png"), "Justify",
                                            lambda: self.editor.setAlignment(Qt.AlignJustify), QKeySequence("Ctrl+J"))
        self.left.setCheckable(True)
        self.center.setCheckable(True)
        self.right.setCheckable(True)
        self.justify.setCheckable(True)

        self.fontbar.addSeparator()
        self.fontbar.addAction(self.left)
        self.fontbar.addAction(self.center)
        self.fontbar.addAction(self.right)
        self.fontbar.addAction(self.justify)

    def init_insert_menu(self):
        self.insertbar = QToolBar()
        self.addToolBar(self.insertbar)
        self.insert_menu = self.menubar.addMenu("&Insert")
        insert_list = self.insert_menu.addAction(QIcon("icons/square-list.png"), "Insert list",
                                                 lambda: self.insert_list(),
                                                 Qt.CTRL + Qt.Key_H)
        insert_img = self.insert_menu.addAction(QIcon("icons/image.png"), "Insert image", lambda: self.insert_image(),
                                                Qt.CTRL + Qt.Key_M)
        insert_table = self.insert_menu.addAction(QIcon("icons/table.png"), "Insert table", lambda: self.insert_table(),
                                                  Qt.CTRL + Qt.Key_T)

        self.insertbar.addAction(insert_table)
        self.insertbar.addAction(insert_list)
        self.insertbar.addAction(insert_img)

    def bold(self):
        if self.editor.fontWeight() == QFont.Bold:
            self.editor.setFontWeight(QFont.Normal)
        else:
            self.editor.setFontWeight(QFont.Bold)

    def italic(self):
        if self.editor.fontItalic():
            self.editor.setFontItalic(False)
        else:
            self.editor.setFontItalic(True)

    def underline(self):
        if self.editor.fontUnderline():
            self.editor.setFontUnderline(False)
        else:
            self.editor.setFontUnderline(True)

    def font_format(self):
        font, ok = self.font_dialog.getFont()
        if ok:
            print(type(font))
            self.font_dialog.setCurrentFont(font)
            self.editor.setFont(font)
            self.fonts.setCurrentFont(font)

    def current_format_changed(self):
        self.font_size_box.setValue(self.editor.currentFont().pointSize())
        self.bold.setChecked(self.editor.fontWeight() == QFont.Bold)
        self.italic.setChecked(self.editor.fontItalic())
        self.underline.setChecked(self.editor.fontUnderline())

        self.color_button.setStyleSheet("background-color:" + self.editor.textColor().name())

    def cursor_position_changed(self):
        self.fonts.setCurrentFont(self.editor.currentFont())
        self.font_size_box.setValue(self.editor.fontPointSize())
        self.left.setChecked(self.editor.alignment() == Qt.AlignLeft)

        self.center.setChecked(self.editor.alignment() == Qt.AlignCenter)

        self.right.setChecked(self.editor.alignment() == Qt.AlignRight)

        self.justify.setChecked(self.editor.alignment() == Qt.AlignJustify)

    def font_color(self, color_button, color_dialog):
        self.editor.setTextColor(color_dialog.getColor())
        color_button.setStyleSheet("background-color:" + self.editor.textColor().name())

    def font_size(self, toolbar):
        self.font_size_box = QSpinBox()
        self.font_size_box.setFixedWidth(48)
        self.font_size_box.setAlignment(Qt.AlignHCenter)
        self.font_size_box.setWrapping(True)
        self.font_size_box.setMaximum(244)
        self.font_size_box.setValue(self.editor.currentFont().pointSize())
        self.font_size_box.valueChanged.connect(self.editor.setFontPointSize)

        toolbar.addWidget(self.font_size_box)

    def save_file(self):
        if self.path == "":
            self.save_file_as()
        else:
            text = self.editor.toHtml()

            try:
                with open(self.path, 'w') as f:
                    f.write(text)
            except Exception as e:
                QtWidgets.QMessageBox.information(self, "Writer", "Error")
                return

    def save_file_as(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", None,
                                              "HTML documents (*.html);;Text documents (*.txt);;All files (*.*);; PDF (*.pdf)")

        if not path:
            return

        text = self.editor.toHtml()

        try:
            with open(path, 'w') as f:
                f.write(text)


        except:
            QtWidgets.QMessageBox.information(self, "Writer", "Не вдалось зберегти файл")

            return

        else:

            self.path = path

    def open_text_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Відкрити файл", QtCore.QDir.homePath(),
                                              "All files (*.*);; HTML (*.html);; DOC (*.doc)")
        if str(path):
            print(path)
            try:
                with open(path, 'rU') as f:
                    text = f.read()

            except:
                QtWidgets.QMessageBox.information(self, "Writer", "Не вдалось відкрити файл")
                return

            self.path = path
            self.editor.setText(text)

    def print(self):
        printer = QPrinter(QPrinter.HighResolution)
        print_menu = QPrintDialog(printer, self)

        if print_menu.exec_() == QPrintDialog.Accepted:
            self.editor.print_(printer)

    def preview(self):
        printer = QPrinter(QPrinter.HighResolution)
        preview_menu = QPrintPreviewDialog(printer, self)
        preview_menu.paintRequested.connect(lambda: self.editor.print_(printer))
        preview_menu.exec_()

    def export_to_pdf(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF(*.pdf)")
        if file_name != "":
            if QFileInfo(file_name).suffix() == "":
                file_name += ".pdf"
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(file_name)
            self.editor.document().print_(printer)

    def insert_image(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Insert image", QtCore.QDir.homePath(),
                                                  "Images (*.png *.xpm *.jpg *.bmp *.gif)")

        if filename:
            image = QImage(filename)

            if image.isNull():

                popup = QMessageBox(QMessageBox.Critical,
                                    "Image load error",
                                    "Could not load image file!",
                                    QMessageBox.Ok,
                                    self)
                popup.show()

            else:
                cursor = self.editor.textCursor()
                cursor.insertImage(image, filename)

    def new_file_event(self):
        if self.editor.document().isModified():
            result = QtWidgets.QMessageBox.question(self,
                                                    "Confirm close",
                                                    "The document has been modified.\n"
                                                    "Do you want to save your changes?",
                                                    QtWidgets.QMessageBox.Save |
                                                    QtWidgets.QMessageBox.Discard |
                                                    QtWidgets.QMessageBox.Cancel)

            if result == QtWidgets.QMessageBox.Discard:
                self.editor.clear()

            elif result == QMessageBox.Save:
                self.save_file()
            else:
                QMessageBox.close()
        else:
            self.editor.clear()
            self.path = ""

    def closeEvent(self, e):
        if self.editor.document().isModified():
            result = QtWidgets.QMessageBox.question(self,
                                                    "Confirm close",
                                                    "The document has been modified.\n"
                                                    "Do you want to save your changes?",
                                                    QtWidgets.QMessageBox.Save |
                                                    QtWidgets.QMessageBox.Discard |
                                                    QtWidgets.QMessageBox.Cancel)

            if result == QtWidgets.QMessageBox.Discard:
                e.accept()
                QtWidgets.QWidget.closeEvent(self, e)

            elif result == QMessageBox.Save:
                self.save_file()
            else:
                e.ignore()

    def insert_table(self):
        table_dialog = TableInsert(self.editor)
        table_dialog.show()

    def insert_list(self):
        list_menu = List(self.editor)
        list_menu.show()
