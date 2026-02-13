from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
import sys

from app.window import MainWindow
from database.db import Database

def main() -> int:
    game_state = Database.load_game_state()
    app = QApplication(sys.argv)
    window = MainWindow(game_state)

    with open("styles/style.css", "r") as f:
        app.setStyleSheet(f.read())

    app.setApplicationName("KC Clicker")
    app.setWindowIcon(QIcon("images/dollar.png"))

    window.show()
    return app.exec(), game_state

if __name__ == "__main__":
    game_state = main()[1]
    Database.save_game_state(game_state)
    
    