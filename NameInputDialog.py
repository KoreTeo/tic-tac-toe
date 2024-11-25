from PyQt5.QtWidgets import QDialog, QLineEdit, QLabel, QPushButton, QVBoxLayout

class NameInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Введите имена игроков")

        self.player1_label = QLabel("Имя игрока 1:")
        self.player1_input = QLineEdit()

        self.player2_label = QLabel("Имя игрока 2:")
        self.player2_input = QLineEdit()

        self.start_button = QPushButton("Начать игру")
        self.start_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.player1_label)
        layout.addWidget(self.player1_input)
        layout.addWidget(self.player2_label)
        layout.addWidget(self.player2_input)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def get_player_names(self):
        return self.player1_input.text(), self.player2_input.text()
