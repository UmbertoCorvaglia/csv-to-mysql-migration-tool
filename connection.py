
from functools import partial
import mysql.connector
from mysql.connector import Error


class Connection:

    def __init__(self, view):
        self._view = view
        self._connectToDB()
    
    def _connectToDB(self):
        pass
        # self._view.pushButton_2.clicked.connect(partial(self._OnConnect))
    
    def _OnConnect(self):

        host = str(self._view.hostLineEdit.text())
        db = str(self._view.databaseLineEdit.text())
        usr = str(self._view.usernameLineEdit.text())
        pwd = str(self._view.passwordLineEdit.text())

        if host == '' and db == '' and usr == '' and pwd == '':
            host = str(self._view.hostLineEdit.placeholderText())
            db = str(self._view.databaseLineEdit.placeholderText())
            usr = str(self._view.usernameLineEdit.placeholderText())
            pwd = str(self._view.passwordLineEdit.placeholderText())

        try:
            connection = mysql.connector.connect(host=host,
                                                database=db,
                                                user=usr,
                                                password=pwd)
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                _string = "Connected to: " + record[0]
                self._view.onConnectLineEdit.setText(_string)
        
        except:
            _string = "Error"
            self._view.onConnectLineEdit.setText(_string)

