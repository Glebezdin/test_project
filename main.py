import sys
from ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import test_file


class TestClass(QtWidgets.QMainWindow):
    def __init__(self):
        super(TestClass, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.ui.pushButton_2.clicked.connect(self.test_main_auth)  # Работает
        self.ui.pushButton.clicked.connect(test_file.test_main_auth_2)  # Не работает

    def test_main_auth(self):
        login = self.ui.lineEdit_2.text()
        print(f'Логин: {login}')  # Могу вывести в консоль значение поля lineEdit_2


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle('Fusion')
    application = TestClass()
    application.show()
    sys.exit(app.exec())