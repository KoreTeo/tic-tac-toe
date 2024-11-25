from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

class SettingsDialog(QDialog):
    def __init__(self, settings, parent=None):
        super().__init__(parent)
        loadUi("settings.ui", self)
        self.settings = settings

        self.rows_input.setText(str(self.settings.value("rows", 10)))
        self.cols_input.setText(str(self.settings.value("cols", 10)))

        self.save_button.clicked.connect(self.save_settings)

    def save_settings(self):
        rows = self.rows_input.text()
        cols = self.cols_input.text()
        if rows.isdigit() and cols.isdigit():
            self.settings.setValue("rows", int(rows))
            self.settings.setValue("cols", int(cols))

            self.accept()
        else:
            QMessageBox.warning(self, "Ошибка", "Введите допустимые размеры поля.")
