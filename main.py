from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
import sys

from app.window import MainWindow
from database.db import Database
from database.game_state import game_state

def load_game_state() -> dict:
    orginal_game_state = game_state()
    try:
        with Database() as db:
            data = db.get_game_state()
            if data:
                return data
            else:
                return orginal_game_state
    except Exception as e:
        print(f"Error loading game state: {e}")
        return orginal_game_state

def save_game_state(game_state: dict) -> None:
    with Database() as db:
        db.add_game_state(game_state)

def main() -> int:
    game_state = load_game_state()
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
    save_game_state(game_state)
    
    