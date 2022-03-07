

from PyQt5 import QtCore, QtGui, QtWidgets
from connection import Connection
import sys
from gui_migration_tool import Ui_MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    Connection(view=ex)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()