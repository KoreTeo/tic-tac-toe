import json
import os
from PyQt5.QtCore import QDate
from PyQt5.QtCore import pyqtSignal, QObject

class GameModelSignals(QObject):
    board_updated = pyqtSignal()
    status_updated = pyqtSignal(str)
    game_over = pyqtSignal(str)

class GameModel:
    def __init__(self, rows=10, cols=10, player_names=None, stats_file="game_stats.json"):
        self.rows = rows
        self.cols = cols
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.current_player = 1
        self.player_names = player_names or {1: "Игрок 1", 2: "Игрок 2"}
        self.stats_file = stats_file
        self.signals = GameModelSignals()

    def reset(self):
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 1
        self.signals.board_updated.emit()
        self.signals.status_updated.emit(self.get_status_message())

    def make_move(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            self.signals.board_updated.emit()
            if self.check_winner(row, col):
                winner_name = self.player_names[self.current_player]
                self.save_game_result(winner_name)
                self.signals.game_over.emit(f"Победил {winner_name}")
                return
            self.current_player = 3 - self.current_player
            self.signals.status_updated.emit(self.get_status_message())
        else:
            self.signals.status_updated.emit("Ячейка занята. Попробуйте другую.")

    def check_winner(self, row, col):
        def count_in_direction(dx, dy):
            count = 0
            x, y = row + dx, col + dy
            while 0 <= x < self.rows and 0 <= y < self.cols and self.board[x][y] == self.current_player:
                count += 1
                x += dx
                y += dy
            return count

        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dx, dy in directions:
            if 1 + count_in_direction(dx, dy) + count_in_direction(-dx, -dy) >= 5:
                return True
        return False

    def get_status_message(self):
        symbol = "X" if self.current_player == 1 else "O"
        return f"Ход {self.player_names[self.current_player]}: {symbol}"

    def save_game_result(self, winner_name):
        stats = []

        if os.path.exists(self.stats_file):
            with open(self.stats_file, "r") as file:
                stats = json.load(file)

        new_record = {
            "player": winner_name,
            "date": QDate.currentDate().toString("yyyy-MM-dd"),
            "size": f"{self.rows}x{self.cols}"
        }
        stats.append(new_record)

        with open(self.stats_file, "w") as file:
            json.dump(stats, file, indent=4)
