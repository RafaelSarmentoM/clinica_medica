from PySide6 import QtCore, QtWidgets
from PES_FSNovo import Ui_Login
from Autenticar_Cat import autenticar, criar_conta
import sys

class Login(QtWidgets.QWidget, Ui_Login):
    logged_in = QtCore.Signal(str, dict)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Tela de Login")

        self.radioButton_P.toggled.connect(self.on_radio_changed)
        self.radioButton_A.toggled.connect(self.on_radio_changed)
        self.radioButton_D.toggled.connect(self.on_radio_changed)

        self.radioButton_P.toggled.connect(lambda: self._on_role_selected("Paciente"))
        self.radioButton_A.toggled.connect(lambda: self._on_role_selected("Admin"))
        self.radioButton_D.toggled.connect(lambda: self._on_role_selected("Doutor"))
    # Conectar botões de login por página
        self.pushButton_1LP.clicked.connect(lambda: self.try_login("Paciente"))
        self.pushButton_2LA.clicked.connect(lambda: self.try_login("Admin"))
        self.pushButton_3LD.clicked.connect(lambda: self.try_login("Doutor"))

        # Inicialização da página em Paciente
        self.radioButton_P.setChecked(True)
        self.stackedWidget.setCurrentIndex(0)


    def on_radio_changed(self):
        if self.radioButton_P.isChecked():
            self.stackedWidget.setCurrentIndex(0)
        elif self.radioButton_A.isChecked():
            self.stackedWidget.setCurrentIndex(1)
        elif self.radioButton_D.isChecked():
            self.stackedWidget.setCurrentIndex(2)

    def _on_role_selected(self, role):
        if role == "Paciente" and self.radioButton_P.isChecked():
            self.stackedWidget.setCurrentIndex(0)
        elif role == "Admin" and self.radioButton_A.isChecked():
            self.stackedWidget.setCurrentIndex(1)
        elif role == "Doutor" and self.radioButton_D.isChecked():
            self.stackedWidget.setCurrentIndex(2)

    def try_login(self, role):
        if role == "Paciente":
            usuario = self.lineEdit_1UP.text()
            senha = self.lineEdit_1SP.text()
        elif role == "Admin":
            usuario = self.lineEdit_2UA.text()
            senha = self.lineEdit_2SA.text()
        else:  # Doutor
            usuario = self.lineEdit_3UD.text()
            senha = self.lineEdit_3SD.text()
            crm_field = getattr(self, "leCRMDoutor", None)
            crm_text = crm_field.text().strip() if crm_field else None

        user_data = autenticar(role, usuario, senha)
        if user_data:
            # Se for doutor, opcionalmente confirmar CRM bate com o dado
            if role == "Doutor" and crm_field:
                expected_crm = user_data.get("crm")
                if expected_crm and crm_text and crm_text != expected_crm:
                    QtWidgets.QMessageBox.warning(self, "Erro", "CRM não confere")
                    return
            self.logged_in.emit(role, user_data)
        else:
            QtWidgets.QMessageBox.warning(self, "Erro", "Usuário ou senha inválidos")

    def create_account_ui(self, role):
        username, ok = QtWidgets.QInputDialog.getText(self, "Cadastro", "Usuário:")
        if not ok or not username:
            return
        password, ok = QtWidgets.QInputDialog.getText(self, "Cadastro", "Senha:", QtWidgets.QLineEdit.Password)
        if not ok or not password:
            return
        extra = {}
        if role == "Doutor":
            crm, ok = QtWidgets.QInputDialog.getText(self, "Cadastro", "CRM:")
            if not ok or not crm:
                return
            extra["crm"] = crm
        success = criar_conta(role, username, password, extra)
        QtWidgets.QMessageBox.information(self, "Cadastro", "Criado com sucesso" if success else "Usuário já existe")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tela = Login()
    tela.show()
    app.exec_()