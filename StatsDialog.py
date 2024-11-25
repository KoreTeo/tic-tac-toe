from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi
import os
import json

class StatsDialog(QDialog):
    def __init__(self, path, parent):
        super().__init__(parent)
        loadUi("stats.ui", self)
        self.close_button.clicked.connect(self.close)
        self.stats_file = path
        self.load_statistics()

    def load_statistics(self):
        stats = []
        if os.path.exists(self.stats_file):
            with open(self.stats_file, "r") as f:
                stats = json.load(f)

        self.stats_table.setRowCount(len(stats))
        for row, stat in enumerate(stats):
            self.stats_table.setItem(row, 0, QTableWidgetItem(stat["player"]))
            self.stats_table.setItem(row, 1, QTableWidgetItem(stat["date"]))
            self.stats_table.setItem(row, 2, QTableWidgetItem(stat["size"]))
