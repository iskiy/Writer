from MainWindow import *


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Writer")
    window.show()
    sys.exit(app.exec_())
