from main import TestClass


def test_main_auth_2():
    ui = TestClass()
    login_2 = ui.ui.lineEdit_2.text()
    print(f'Логин: {login_2}')  # Не могу вывести в консоль значение поля lineEdit_2