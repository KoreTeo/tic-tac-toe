# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(300, 200)
        self.verticalLayout = QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_rows = QLabel(SettingsDialog)
        self.label_rows.setObjectName(u"label_rows")

        self.verticalLayout.addWidget(self.label_rows)

        self.rows_input = QLineEdit(SettingsDialog)
        self.rows_input.setObjectName(u"rows_input")

        self.verticalLayout.addWidget(self.rows_input)

        self.label_cols = QLabel(SettingsDialog)
        self.label_cols.setObjectName(u"label_cols")

        self.verticalLayout.addWidget(self.label_cols)

        self.cols_input = QLineEdit(SettingsDialog)
        self.cols_input.setObjectName(u"cols_input")

        self.verticalLayout.addWidget(self.cols_input)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.save_button = QPushButton(SettingsDialog)
        self.save_button.setObjectName(u"save_button")

        self.buttonLayout.addWidget(self.save_button)

        self.cancel_button = QPushButton(SettingsDialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.buttonLayout.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(SettingsDialog)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_rows.setText(QCoreApplication.translate("SettingsDialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0440\u043e\u043a:", None))
        self.rows_input.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0440\u043e\u043a (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, 10)", None))
        self.label_cols.setText(QCoreApplication.translate("SettingsDialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432:", None))
        self.cols_input.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432 (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, 10)", None))
        self.save_button.setText(QCoreApplication.translate("SettingsDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancel_button.setText(QCoreApplication.translate("SettingsDialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
#if QT_CONFIG(shortcut)
        self.cancel_button.setShortcut(QCoreApplication.translate("SettingsDialog", u"Esc", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

