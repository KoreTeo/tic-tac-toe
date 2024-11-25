from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout, QMessageBox, QStatusBar



class GameWindow(QMainWindow):
    def __init__(self, model, parent=None):
        super().__init__(parent)

        self.model = model

        self.model.signals.board_updated.connect(self.update_board)
        self.model.signals.status_updated.connect(self.update_status)
        self.model.signals.game_over.connect(self.end_game)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Игра 5 в ряд")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout(central_widget)

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)
        self.buttons = [[QPushButton("") for _ in range(self.model.cols)] for _ in range(self.model.rows)]
        for i in range(self.model.rows):
            for j in range(self.model.cols):
                button = self.buttons[i][j]
                button.setFixedSize(40, 40)
                button.clicked.connect(lambda _, x=i, y=j: self.model.make_move(x, y))
                self.grid_layout.addWidget(button, i, j)

        self.quit_button = QPushButton("Выйти в главное меню", self)
        self.quit_button.clicked.connect(self.quit_game)
        self.layout.addWidget(self.quit_button)

        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

        self.model.reset()

    def update_board(self):
        for i in range(self.model.rows):
            for j in range(self.model.cols):
                value = self.model.board[i][j]
                self.buttons[i][j].setText("X" if value == 1 else "O" if value == 2 else "")

    def update_status(self, message):
        self.status_bar.showMessage(message)

    def end_game(self, message):
        QMessageBox.information(self, "Игра окончена", message)
        self.model.reset()

    def quit_game(self):
        self.close()
        self.parent().show()

