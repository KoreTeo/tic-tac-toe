from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import QSettings
from SettingsDialog import SettingsDialog
from StatsDialog import StatsDialog
from GameWindow import GameWindow
from GameModel import GameModel
from NameInputDialog import NameInputDialog
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.settings = QSettings("settings.ini", QSettings.IniFormat)
        self.game_window = None
        self.game_model = None

        loadUi("main_window.ui", self)

        self.apply_styles()

        self.start_button.clicked.connect(self.start_game)
        self.settings_button.clicked.connect(self.open_settings)
        self.stats_button.clicked.connect(self.open_stats)

    def apply_styles(self):
        with open("styles.qss", "r") as file:
            self.setStyleSheet(file.read())

    def start_game(self):
        dialog = NameInputDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            player1_name, player2_name = dialog.get_player_names()

            rows = int(self.settings.value("rows", 10))
            cols = int(self.settings.value("cols", 10))
            self.game_model = GameModel(rows, cols, {1: player1_name, 2: player2_name})

            self.hide()
            if self.game_window:
                self.game_window.close()
            self.game_window = GameWindow(self.game_model, self)
            self.game_window.show()

    def open_settings(self):
        settings_dialog = SettingsDialog(self.settings, self)
        settings_dialog.exec_()

    def open_stats(self):
        stats_dialog = StatsDialog("game_stats.json", self)
        stats_dialog.exec_()

