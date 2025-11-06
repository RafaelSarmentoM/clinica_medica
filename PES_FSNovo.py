# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PES_FSNovo.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(949, 583)
        Login.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(85, 255, 255), stop:1 rgb(85, 255, 127));")
        self.horizontalLayout_3 = QHBoxLayout(Login)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, -1, -1, -1)
        self.widget = QWidget(Login)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: transparent")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(63, -1, -1, -1)
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(200, 0))
        self.groupBox.setMaximumSize(QSize(16777215, 150))
        self.groupBox.setStyleSheet(u"background-color: rgb(215, 215, 215);\n"
"\n"
"border-radius: 30px")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(63, -1, -1, -1)
        self.radioButton_P = QRadioButton(self.groupBox)
        self.radioButton_P.setObjectName(u"radioButton_P")

        self.verticalLayout_2.addWidget(self.radioButton_P)

        self.radioButton_A = QRadioButton(self.groupBox)
        self.radioButton_A.setObjectName(u"radioButton_A")

        self.verticalLayout_2.addWidget(self.radioButton_A)

        self.radioButton_D = QRadioButton(self.groupBox)
        self.radioButton_D.setObjectName(u"radioButton_D")

        self.verticalLayout_2.addWidget(self.radioButton_D)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.horizontalLayout_3.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(Login)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setMaximumSize(QSize(600, 16777215))
        self.stackedWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.stackedWidget.setStyleSheet(u"background-color: transparent")
        self.page_1_LP = QWidget()
        self.page_1_LP.setObjectName(u"page_1_LP")
        self.verticalLayout_4 = QVBoxLayout(self.page_1_LP)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_1 = QFrame(self.page_1_LP)
        self.frame_1.setObjectName(u"frame_1")
        sizePolicy1.setHeightForWidth(self.frame_1.sizePolicy().hasHeightForWidth())
        self.frame_1.setSizePolicy(sizePolicy1)
        self.frame_1.setMinimumSize(QSize(400, 0))
        self.frame_1.setMaximumSize(QSize(500, 16777215))
        self.frame_1.setStyleSheet(u"background-color: rgb(170, 170, 170);\n"
"\n"
"\n"
"border-radius: 50px\n"
"")
        self.frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 40, -1, 90)
        self.lineEdit_1UP = QLineEdit(self.frame_1)
        self.lineEdit_1UP.setObjectName(u"lineEdit_1UP")
        self.lineEdit_1UP.setMinimumSize(QSize(200, 0))
        self.lineEdit_1UP.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.lineEdit_1UP.setFont(font)
        self.lineEdit_1UP.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:rgb(18, 18, 18);\n"
"border-radius:10px")
        self.lineEdit_1UP.setText(u"")
        self.lineEdit_1UP.setFrame(True)
        self.lineEdit_1UP.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_1UP.setClearButtonEnabled(False)

        self.verticalLayout_6.addWidget(self.lineEdit_1UP, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_1SP = QLineEdit(self.frame_1)
        self.lineEdit_1SP.setObjectName(u"lineEdit_1SP")
        self.lineEdit_1SP.setMinimumSize(QSize(200, 0))
        self.lineEdit_1SP.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_1SP.setFont(font)
        self.lineEdit_1SP.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_1SP.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(18, 18, 18);\n"
"border-radius:10px")
        self.lineEdit_1SP.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_1SP.setDragEnabled(False)

        self.verticalLayout_6.addWidget(self.lineEdit_1SP, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_1LP = QPushButton(self.frame_1)
        self.pushButton_1LP.setObjectName(u"pushButton_1LP")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_1LP.sizePolicy().hasHeightForWidth())
        self.pushButton_1LP.setSizePolicy(sizePolicy2)
        self.pushButton_1LP.setMinimumSize(QSize(250, 40))
        self.pushButton_1LP.setMaximumSize(QSize(200, 50))
        self.pushButton_1LP.setFont(font)
        self.pushButton_1LP.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(120, 120, 120);\n"
"border-radius:10px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(80, 80, 80);\n"
"\n"
"border-radius:10px\n"
"\n"
"}")

        self.verticalLayout_6.addWidget(self.pushButton_1LP, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_1CP = QPushButton(self.frame_1)
        self.pushButton_1CP.setObjectName(u"pushButton_1CP")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_1CP.sizePolicy().hasHeightForWidth())
        self.pushButton_1CP.setSizePolicy(sizePolicy3)
        self.pushButton_1CP.setMinimumSize(QSize(250, 40))
        self.pushButton_1CP.setMaximumSize(QSize(200, 50))
        self.pushButton_1CP.setFont(font)
        self.pushButton_1CP.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(120, 120, 120);\n"
"border-radius:10px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(80, 80, 80);\n"
"\n"
"border-radius:10px\n"
"\n"
"}")

        self.verticalLayout_6.addWidget(self.pushButton_1CP, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_1, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget.addWidget(self.page_1_LP)
        self.page_2_LA = QWidget()
        self.page_2_LA.setObjectName(u"page_2_LA")
        self.horizontalLayout = QHBoxLayout(self.page_2_LA)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.page_2_LA)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(400, 0))
        self.frame_2.setMaximumSize(QSize(500, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(170, 170, 170);\n"
"\n"
"\n"
"border-radius: 50px")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 40, -1, 90)
        self.lineEdit_2UA = QLineEdit(self.frame_2)
        self.lineEdit_2UA.setObjectName(u"lineEdit_2UA")
        self.lineEdit_2UA.setMinimumSize(QSize(200, 0))
        self.lineEdit_2UA.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_2UA.setFont(font)
        self.lineEdit_2UA.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:rgb(18, 18, 18);\n"
"border-radius:10px")
        self.lineEdit_2UA.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.lineEdit_2UA, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_2SA = QLineEdit(self.frame_2)
        self.lineEdit_2SA.setObjectName(u"lineEdit_2SA")
        self.lineEdit_2SA.setMinimumSize(QSize(200, 0))
        self.lineEdit_2SA.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_2SA.setFont(font)
        self.lineEdit_2SA.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_2SA.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:rgb(18, 18, 18);\n"
"border-radius:10px")
        self.lineEdit_2SA.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2SA.setDragEnabled(False)

        self.verticalLayout_5.addWidget(self.lineEdit_2SA, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_2LA = QPushButton(self.frame_2)
        self.pushButton_2LA.setObjectName(u"pushButton_2LA")
        sizePolicy2.setHeightForWidth(self.pushButton_2LA.sizePolicy().hasHeightForWidth())
        self.pushButton_2LA.setSizePolicy(sizePolicy2)
        self.pushButton_2LA.setMinimumSize(QSize(250, 40))
        self.pushButton_2LA.setMaximumSize(QSize(200, 50))
        self.pushButton_2LA.setFont(font)
        self.pushButton_2LA.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(120, 120, 120);\n"
"border-radius:10px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(80, 80, 80);\n"
"\n"
"border-radius:10px\n"
"\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton_2LA, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_2CA = QPushButton(self.frame_2)
        self.pushButton_2CA.setObjectName(u"pushButton_2CA")
        sizePolicy3.setHeightForWidth(self.pushButton_2CA.sizePolicy().hasHeightForWidth())
        self.pushButton_2CA.setSizePolicy(sizePolicy3)
        self.pushButton_2CA.setMinimumSize(QSize(250, 40))
        self.pushButton_2CA.setMaximumSize(QSize(200, 50))
        self.pushButton_2CA.setFont(font)
        self.pushButton_2CA.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(120, 120, 120);\n"
"border-radius:10px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(80, 80, 80);\n"
"\n"
"border-radius:10px\n"
"\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton_2CA, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget.addWidget(self.page_2_LA)
        self.page_3_LD = QWidget()
        self.page_3_LD.setObjectName(u"page_3_LD")
        self.horizontalLayout_2 = QHBoxLayout(self.page_3_LD)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_3 = QFrame(self.page_3_LD)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(400, 0))
        self.frame_3.setMaximumSize(QSize(500, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgb(170, 170, 170);\n"
"\n"
"\n"
"border-radius: 50px")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 40, -1, 90)
        self.lineEdit_3UD = QLineEdit(self.frame_3)
        self.lineEdit_3UD.setObjectName(u"lineEdit_3UD")
        self.lineEdit_3UD.setMinimumSize(QSize(200, 0))
        self.lineEdit_3UD.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_3UD.setFont(font)
        self.lineEdit_3UD.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:rgb(18, 18, 18);\n"
"border-radius:10px")
        self.lineEdit_3UD.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_3UD, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_3SD = QLineEdit(self.frame_3)
        self.lineEdit_3SD.setObjectName(u"lineEdit_3SD")
        self.lineEdit_3SD.setMinimumSize(QSize(200, 0))
        self.lineEdit_3SD.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_3SD.setFont(font)
        self.lineEdit_3SD.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_3SD.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:rgb(18, 18, 18);\n"
"border-radius:10px")
        self.lineEdit_3SD.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3SD.setDragEnabled(False)

        self.verticalLayout.addWidget(self.lineEdit_3SD, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_3CRM = QLineEdit(self.frame_3)
        self.lineEdit_3CRM.setObjectName(u"lineEdit_3CRM")
        self.lineEdit_3CRM.setMinimumSize(QSize(200, 0))
        self.lineEdit_3CRM.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_3CRM.setFont(font)
        self.lineEdit_3CRM.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:rgb(18, 18, 18);\n"
"border-radius:10px")
        self.lineEdit_3CRM.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_3CRM, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_3LD = QPushButton(self.frame_3)
        self.pushButton_3LD.setObjectName(u"pushButton_3LD")
        sizePolicy2.setHeightForWidth(self.pushButton_3LD.sizePolicy().hasHeightForWidth())
        self.pushButton_3LD.setSizePolicy(sizePolicy2)
        self.pushButton_3LD.setMinimumSize(QSize(250, 40))
        self.pushButton_3LD.setMaximumSize(QSize(200, 50))
        self.pushButton_3LD.setFont(font)
        self.pushButton_3LD.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(120, 120, 120);\n"
"border-radius:10px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(80, 80, 80);\n"
"\n"
"border-radius:10px\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_3LD, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_3CD = QPushButton(self.frame_3)
        self.pushButton_3CD.setObjectName(u"pushButton_3CD")
        sizePolicy3.setHeightForWidth(self.pushButton_3CD.sizePolicy().hasHeightForWidth())
        self.pushButton_3CD.setSizePolicy(sizePolicy3)
        self.pushButton_3CD.setMinimumSize(QSize(250, 40))
        self.pushButton_3CD.setMaximumSize(QSize(200, 50))
        self.pushButton_3CD.setFont(font)
        self.pushButton_3CD.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(120, 120, 120);\n"
"border-radius:10px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(80, 80, 80);\n"
"\n"
"border-radius:10px\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_3CD, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget.addWidget(self.page_3_LD)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.retranslateUi(Login)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.groupBox.setTitle("")
        self.radioButton_P.setText(QCoreApplication.translate("Login", u"Paciente", None))
        self.radioButton_A.setText(QCoreApplication.translate("Login", u"Admin", None))
        self.radioButton_D.setText(QCoreApplication.translate("Login", u"Doutor", None))
        self.lineEdit_1UP.setPlaceholderText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.lineEdit_1SP.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.pushButton_1LP.setText(QCoreApplication.translate("Login", u"Login", None))
        self.pushButton_1CP.setText(QCoreApplication.translate("Login", u"Cadastro", None))
        self.lineEdit_2UA.setPlaceholderText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.lineEdit_2SA.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.pushButton_2LA.setText(QCoreApplication.translate("Login", u"Login", None))
        self.pushButton_2CA.setText(QCoreApplication.translate("Login", u"Cadastro", None))
        self.lineEdit_3UD.setPlaceholderText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.lineEdit_3SD.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.lineEdit_3CRM.setPlaceholderText(QCoreApplication.translate("Login", u"CRM", None))
        self.pushButton_3LD.setText(QCoreApplication.translate("Login", u"Login", None))
        self.pushButton_3CD.setText(QCoreApplication.translate("Login", u"Cadastro", None))
    # retranslateUi

