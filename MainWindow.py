import sys
from PySide6 import QtWidgets
from login import Login
from PES_MW import Ui_MainWindow  

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, role, user_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.role = role
        self.user = user_data
        # exemplo de configuração: ajuste objectName do label no designer
        label = getattr(self.ui, "labelUser", None)
        if label:
            label.setText(f"{user_data.get('full_name', user_data.get('username'))} ({role})")

def main():
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    main_win = None

    def on_logged_in(role, user_data):
        nonlocal main_win
        login.close()
        main_win = MainWindow(role, user_data)
        main_win.show()

    login.logged_in.connect(on_logged_in)
    login.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()