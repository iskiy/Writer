from PyQt5.QtCore import Qt, QFileInfo, QSize
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog

from List import List
from TableInsert import TableInsert
from TextEdit import *


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        self.edit_menu = \
            self.file_bar = \
            self.font_menu = \
            self.font_dialog = \
            self.font_bar = \
            self.fonts = \
            self.font_size_box = \
            self.color_font_dialog = \
            self.color_button = \
            self.color_font_background_dialog = \
            self.background_color_button = \
            self.right = \
            self.center = \
            self.left = \
            self.justify = \
            self.bold = \
            self.italic = \
            self.underline = \
            self.strikeout = \
            self.insert_bar = \
            self.insert_menu = \
            self.line_wrap_mode = \
            super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon("icons/write.png"))
        self.BAR_ICON_SIZE = 36
        self.editor = TextEdit()
        self.setCentralWidget(self.editor)
        self.path = ""
        self.menu_bar = self.menuBar()
        self.menu_bar.setStyleSheet("background-color: #BFA97B; border: 2px solid #A67E2B")
        self.init_bars()
        self.init_file_menu()
        self.init_edit_menu()
        self.init_font_menu()
        self.init_align_menu()
        self.init_insert_menu()

        self.editor.currentCharFormatChanged.connect(self.current_format_changed)
        self.editor.cursorPositionChanged.connect(self.cursor_position_changed)

    def init_bars(self):
        color = 'QToolBar {background-color:#BF9A7B; border: 2px solid #BF9A7B;} QToolButton:hover {' \
                'background-color:#2CA0A6} '
        self.file_bar = QToolBar()
        self.file_bar.setStyleSheet(str(color))
        self.file_bar.setIconSize(QSize(self.BAR_ICON_SIZE, self.BAR_ICON_SIZE))
        self.font_bar = QToolBar()
        self.font_bar.setStyleSheet(str(color))
        self.font_bar.setIconSize(QSize(self.BAR_ICON_SIZE, self.BAR_ICON_SIZE))
        self.insert_bar = QToolBar()
        self.insert_bar.setStyleSheet(str(color))
        self.insert_bar.setIconSize(QSize(self.BAR_ICON_SIZE, self.BAR_ICON_SIZE))

    def init_file_menu(self):
        file_menu = self.menu_bar.addMenu("&File")

        new_file_action = file_menu.addAction(QIcon("icons/new.png"), "New file", self.new_file_event,
                                              QKeySequence.New)

        open_file_action = file_menu.addAction(QIcon("icons/open.png"), "Open file", self.open_text_file,
                                               QKeySequence.Open)

        save_file = file_menu.addAction(QIcon("icons/save.png"), "Save file", self.save_file,
                                        QKeySequence.Save)

        save_file_as = file_menu.addAction(QIcon("icons/save_as.png"), "Save as..", self.save_file_as,
                                           QtCore.Qt.CTRL + QtCore.Qt.ALT + QtCore.Qt.Key_S)

        file_menu.addSeparator()

        print_file = file_menu.addAction(QIcon("icons/print.png"), "Print", self.print,
                                         QKeySequence.Print)

        print_preview = file_menu.addAction(QIcon("icons/preview.png"), "Print preview", self.preview,
                                            QtCore.Qt.CTRL + QtCore.Qt.Key_K)

        export_pdf = file_menu.addAction(QIcon("icons/pdf.png"), "Export PDF", self.export_to_pdf)
        file_menu.addSeparator()

        file_menu.addAction(QIcon("icons/close.png"), "Close", self.close,
                            QKeySequence.Close)

        self.addToolBar(self.file_bar)
        self.file_bar.addAction(new_file_action)
        self.file_bar.addAction(open_file_action)
        self.file_bar.addAction(save_file)
        self.file_bar.addAction(save_file_as)
        self.file_bar.addSeparator()
        self.file_bar.addAction(print_file)
        self.file_bar.addAction(print_preview)
        self.file_bar.addAction(export_pdf)

    def init_edit_menu(self):
        self.edit_menu = self.menu_bar.addMenu("&Edit")
        undo = self.edit_menu.addAction(QIcon("icons/undo.png"), "Undo", self.editor.undo, QKeySequence.Undo)
        redo = self.edit_menu.addAction(QIcon("icons/redo.png"), "Redo", self.editor.redo, QKeySequence.Redo)
        copy = self.edit_menu.addAction(QIcon("icons/copy.png"), "Copy", self.editor.copy, QKeySequence.Copy)
        paste = self.edit_menu.addAction(QIcon("icons/paste.png"), "Paste", self.editor.paste,
                                         QKeySequence.Paste)
        cut = self.edit_menu.addAction(QIcon("icons/cut.png"), "Cut", self.editor.cut, QKeySequence.Cut)
        self.edit_menu.addSeparator()
        self.line_wrap_mode = self.edit_menu.addAction(QIcon("icons/hastag.png"), "Change line wrap mode",
                                                       self.change_line_wrap_mode)
        self.line_wrap_mode.setToolTip("If active then automatic line feed is active,"
                                       " but it is only visual")

        self.line_wrap_mode.setCheckable(True)
        self.line_wrap_mode.setChecked(True)

        self.file_bar.addSeparator()
        self.file_bar.addAction(undo)
        self.file_bar.addAction(redo)
        self.file_bar.addAction(copy)
        self.file_bar.addAction(paste)
        self.file_bar.addAction(cut)
        self.file_bar.addAction(self.line_wrap_mode)

    def init_font_menu(self):
        self.font_menu = self.menu_bar.addMenu("&Font")
        self.font_dialog = QFontDialog()
        self.font_menu.addAction(QIcon("icons/font.png"), "Change font format", self.font_format)

        self.addToolBar(self.font_bar)
        self.fonts = QFontComboBox()
        self.fonts.setFixedHeight(self.BAR_ICON_SIZE * 0.8)
        self.fonts.setStyleSheet("background-color: #FFFFFF")
        self.fonts.setCurrentFont(self.editor.font())
        self.fonts.currentFontChanged.connect(lambda: self.editor.setCurrentFont(self.fonts.currentFont()))
        self.font_bar.addWidget(self.fonts)
        self.font_size(self.font_bar)

        self.color_font_dialog = QColorDialog()
        self.color_button = QPushButton()
        self.color_button.setToolTip("Font color")
        self.color_button.setFixedHeight(self.BAR_ICON_SIZE)
        self.color_button.setFixedWidth(self.BAR_ICON_SIZE * 1.5)
        self.font_bar.addAction(QIcon("icons/font-color.png"), "Font color",
                                lambda: self.font_color(self.color_button, self.color_font_dialog, False))
        self.color_button.clicked.connect(lambda: self.font_color(self.color_button, self.color_font_dialog, False))
        self.font_bar.addWidget(self.color_button)

        self.color_font_background_dialog = QColorDialog()
        self.background_color_button = QPushButton()
        self.background_color_button.setFixedHeight(self.BAR_ICON_SIZE)
        self.background_color_button.setFixedWidth(self.BAR_ICON_SIZE * 1.5)
        self.font_bar.addAction(QIcon("icons/highlight.png"), "Background font color",
                                lambda: self.font_color(self.background_color_button,
                                                        self.color_font_background_dialog,
                                                        True))

        self.background_color_button.clicked.connect(
            lambda: self.font_color(self.background_color_button, self.color_font_background_dialog,
                                    True))
        self.background_color_button.setToolTip("Background font color")

        self.font_bar.addWidget(self.background_color_button)
        self.font_bar.addSeparator()
        bold_ic = QIcon("icons/bold.png")
        self.bold = self.font_bar.addAction(bold_ic, "Bold", self.set_bold)
        self.bold.setShortcut(QKeySequence.Bold)

        self.italic = self.font_bar.addAction(QIcon("icons/italic.png"), "Italic", self.set_italic)
        self.italic.setShortcut(QKeySequence.Italic)

        self.underline = self.font_bar.addAction(QIcon("icons/underline.png"), "Underline", self.set_underline)
        self.underline.setShortcut(QKeySequence.Italic)

        self.strikeout = self.font_bar.addAction(QIcon("icons/strike.png"), "Strikeout", self.set_strikeout)
        self.strikeout.setShortcut(Qt.CTRL + Qt.Key_W)

        self.bold.setCheckable(True)
        self.italic.setCheckable(True)
        self.underline.setCheckable(True)
        self.strikeout.setCheckable(True)

    def init_align_menu(self):
        align_menu = self.menu_bar.addMenu("&Align")

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

        self.font_bar.addSeparator()
        self.font_bar.addAction(self.left)
        self.font_bar.addAction(self.center)
        self.font_bar.addAction(self.right)
        self.font_bar.addAction(self.justify)

    def init_insert_menu(self):

        self.addToolBar(self.insert_bar)
        self.insert_menu = self.menu_bar.addMenu("&Insert")
        insert_list = self.insert_menu.addAction(QIcon("icons/list.png"), "Insert list",
                                                 lambda: self.insert_list(),
                                                 Qt.CTRL + Qt.Key_H)
        insert_img = self.insert_menu.addAction(QIcon("icons/image.png"), "Insert image", lambda: self.insert_image(),
                                                Qt.CTRL + Qt.Key_M)
        insert_table = self.insert_menu.addAction(QIcon("icons/table.png"), "Insert table", lambda: self.insert_table(),
                                                  Qt.CTRL + Qt.Key_T)

        self.insert_bar.addAction(insert_table)
        self.insert_bar.addAction(insert_list)
        self.insert_bar.addAction(insert_img)

    def set_bold(self):
        if self.editor.fontWeight() == QFont.Bold:
            self.editor.setFontWeight(QFont.Normal)
        else:
            self.editor.setFontWeight(QFont.Bold)

    def set_italic(self):
        if self.editor.fontItalic():
            self.editor.setFontItalic(False)
        else:
            self.editor.setFontItalic(True)

    def set_strikeout(self):
        current_format = self.editor.currentCharFormat()
        if current_format.fontStrikeOut():
            current_format.setFontStrikeOut(False)
        else:
            current_format.setFontStrikeOut(True)
        self.editor.setCurrentCharFormat(current_format)

    def set_underline(self):
        if self.editor.fontUnderline():
            self.editor.setFontUnderline(False)
        else:
            self.editor.setFontUnderline(True)

    def font_format(self):
        font, ok = self.font_dialog.getFont()
        if ok:
            self.font_dialog.setCurrentFont(font)
            self.editor.setCurrentFont(font)
            self.fonts.setCurrentFont(font)

    def current_format_changed(self):
        if not self.editor.textCursor().hasSelection():
            current_format = self.editor.currentCharFormat()
            self.font_size_box.setValue(self.editor.currentFont().pointSize())
            self.bold.setChecked(self.editor.fontWeight() == QFont.Bold)
            self.italic.setChecked(self.editor.fontItalic())
            self.underline.setChecked(self.editor.fontUnderline())
            self.strikeout.setChecked(current_format.fontStrikeOut())
            self.color_button.setStyleSheet("background-color:" + self.editor.textColor().name())
            self.background_color_button.setStyleSheet("background-color:" + self.editor.textBackgroundColor().name())

    def cursor_position_changed(self):
        if not self.editor.textCursor().hasSelection():
            self.fonts.setCurrentFont(self.editor.currentFont())
            self.font_size_box.setValue(self.editor.fontPointSize())
            self.left.setChecked(self.editor.alignment() == Qt.AlignLeft)

            self.center.setChecked(self.editor.alignment() == Qt.AlignCenter)

            self.right.setChecked(self.editor.alignment() == Qt.AlignRight)

            self.justify.setChecked(self.editor.alignment() == Qt.AlignJustify)

    def font_color(self, color_button, color_dialog, background_color: bool):
        if background_color:
            self.editor.setTextBackgroundColor(color_dialog.getColor())
            color_button.setStyleSheet("background-color:" + self.editor.textBackgroundColor().name())
        else:
            self.editor.setTextColor(color_dialog.getColor())
            color_button.setStyleSheet("background-color:" + self.editor.textColor().name())

    def font_size(self, toolbar):
        self.font_size_box = QSpinBox()
        self.font_size_box.setFixedHeight(self.BAR_ICON_SIZE * 0.8)
        self.font_size_box.setStyleSheet("background-color: #FFFFFF")
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
            except Exception:
                QtWidgets.QMessageBox.information(self, "Writer", "Error")
                return

    def save_file_as(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "",
                                              "HTML documents (*.html);;Text documents (*.txt);;All files (*.*);; PDF "
                                              "(*.pdf)")

        if not path:
            return

        text = self.editor.toHtml()

        try:
            with open(path, 'w') as f:
                f.write(text)

        except ImportError:
            QtWidgets.QMessageBox.information(self, "Writer", "Не вдалось зберегти файл")

            return

        else:

            self.path = path

    def open_text_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Відкрити файл", QtCore.QDir.homePath(),
                                              "All files (*.*);; HTML (*.html);; DOC (*.doc)")
        if str(path):
            try:
                with open(path, 'rU') as f:
                    text = f.read()

            except ImportError:
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
        file_name, _ = QFileDialog.getSaveFileName(self, "Export PDF", "", "PDF(*.pdf)")
        if file_name != "":
            if QFileInfo(file_name).suffix() == "":
                file_name += ".pdf"
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(file_name)
            self.editor.document().print_(printer)

    def insert_image(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Insert image", QtCore.QDir.homePath(),
                                                  "All images (*.png *.xpm *.jpg *.bmp *.gif);; PNG (*.png);; "
                                                  "(*.jpg);; XPM (*.xpm);; BMP (*.bmp);; GIF (*.gif)")

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

    def change_line_wrap_mode(self):
        if self.editor.lineWrapMode() != QTextEdit.NoWrap:
            self.editor.setLineWrapMode(QTextEdit.NoWrap)
            self.line_wrap_mode.setChecked(False)
        elif self.editor.lineWrapMode() == QTextEdit.NoWrap:
            self.editor.setLineWrapMode(QTextEdit.WidgetWidth)
            self.line_wrap_mode.setChecked(True)

    def insert_table(self):
        table_dialog = TableInsert(self.editor)
        table_dialog.show()

    def insert_list(self):
        list_menu = List(self.editor)
        list_menu.show()
