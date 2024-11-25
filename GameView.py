from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QMessageBox

class GameView(QWidget):
    def __init__(self, model, parent=None, status_bar=None, player1_name="Игрок 1", player2_name="Игрок 2"):
        super().__init__(parent)
        self.parent_window = self.parent()
        self.model = model
        self.status_bar = status_bar  # Используем status_bar из родительского окна
        self.player_names = [player1_name, player2_name]  # Сохраняем имена игроков
        self.init_ui()

    def init_ui(self):
        self.grid_layout = QGridLayout(self)
        self.buttons = [[QPushButton("") for _ in range(self.model.cols)] for _ in range(self.model.rows)]

        # Размещение кнопок для игрового поля
        for i in range(self.model.rows):
            for j in range(self.model.cols):
                button = self.buttons[i][j]
                button.setFixedSize(40, 40)
                button.clicked.connect(self.make_move(i, j))
                self.grid_layout.addWidget(button, i, j)

        # Обновляем статус после загрузки поля
        self.update_status()

    def make_move(self, row, col):
        def handler():
            result = self.model.make_move(row, col)
            self.update_board()
            if result == 0:
                QMessageBox.information(self, "Пу-пу-пу", 'Ячейка занята')
            elif result == 1:
                QMessageBox.information(self, "Игра окончена", f'Победли {self.player_names[0]}')
                self.save_result()
                self.model.reset()
                self.update_board()
            elif result == 2:
                QMessageBox.information(self, "Игра окончена", f'Победли {self.player_names[1]}')
                self.save_result()
                self.model.reset()
                self.update_board()
            self.update_status()

        return handler

    def update_board(self):
        for i in range(self.model.rows):
            for j in range(self.model.cols):
                value = self.model.board[i][j]
                self.buttons[i][j].setText("X" if value == 1 else "O" if value == 2 else "")

    def update_status(self):
        current_player_name = self.player_names[self.model.current_player - 1]
        current_symbol = "X" if self.model.current_player == 1 else "O"
        self.status_bar.showMessage(f"Ход {current_player_name}: {current_symbol}")

    def save_result(self):
        # Сохранение результата игры
        winner_name = self.player_names[self.model.current_player  - 1]

        self.parent_window.save_game_result(winner_name)  # Вызываем метод родительского окна для записи статистики
        def save_game_result(self, winner_name):
                stats = []

                 Загрузка текущей статистики из файла, если он существует
                if os.path.exists(self.stats_file):
                    with open(self.stats_file, "r") as file:
                        stats = json.load(file)

                # Добавление новой записи
                new_record = {
                    "player": winner_name,
                    "date": QDate.currentDate().toString("yyyy-MM-dd"),
                    "size": f"{self.model.rows}x{self.model.cols}"
                }
                stats.append(new_record)

                # Запись обновленных данных обратно в файл
                with open(self.stats_file, "w") as file:
                    json.dump(stats, file, indent=4)
