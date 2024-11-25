# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stats.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_StatsDialog(object):
    def setupUi(self, StatsDialog):
        if not StatsDialog.objectName():
            StatsDialog.setObjectName(u"StatsDialog")
        StatsDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(StatsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stats_table = QTableWidget(StatsDialog)
        if (self.stats_table.columnCount() < 3):
            self.stats_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.stats_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.stats_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.stats_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.stats_table.setObjectName(u"stats_table")
        self.stats_table.setColumnCount(3)
        self.stats_table.setRowCount(0)

        self.verticalLayout.addWidget(self.stats_table)

        self.close_button = QPushButton(StatsDialog)
        self.close_button.setObjectName(u"close_button")

        self.verticalLayout.addWidget(self.close_button)


        self.retranslateUi(StatsDialog)

        QMetaObject.connectSlotsByName(StatsDialog)
    # setupUi

    def retranslateUi(self, StatsDialog):
        StatsDialog.setWindowTitle(QCoreApplication.translate("StatsDialog", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        ___qtablewidgetitem = self.stats_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StatsDialog", u"\u0418\u0433\u0440\u043e\u043a", None));
        ___qtablewidgetitem1 = self.stats_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StatsDialog", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem2 = self.stats_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("StatsDialog", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043f\u043e\u043b\u044f", None));
        self.close_button.setText(QCoreApplication.translate("StatsDialog", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

