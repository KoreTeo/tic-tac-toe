from PyQt5.QtWidgets import QApplication
import sys
from MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_widget = MainWindow()
    main_widget.resize(300, 150)
    main_widget.show()
    sys.exit(app.exec_())
