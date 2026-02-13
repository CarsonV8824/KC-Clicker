from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
import sys

from app.window import MainWindow
from database.db import Database


def load_game_state() -> dict:
    orginal_game_state = {"money": 0, "money_per_second": 0, "Click":1, "houses":{"Troost":{"owned":0, "price": 10, "per_second": 1}, "39th": {"owned":0, "price": 100, "per_second": 2}, "Paseo": {"owned":0, "price": 500, "per_second": 5}, "Wornall": {"owned":0, "price": 1000, "per_second": 10}, "Roanoke": {"owned":0, "price": 5000, "per_second": 20}, "ward": {"owned":0, "price": 10000, "per_second": 50}, "westport": {"owned":0, "price":50000, "per_second":100}, "main": {"owned":0, "price":100000, "per_second": 500}},
                "upgrades": {"Clicked":{"owned": False, "price": 50}, "Troost house upgrade": {"owned": False, "price": 250}, "39th house upgrade": {"owned": False, "price": 500}, "Paseo house upgrade": {"owned": False, "price": 1000}, "Wornall house upgrade": {"owned": False, "price": 1500}, "Roanoke house upgrade": {"owned": False, "price": 2000}, "ward house upgrade": {"owned": False, "price": 5000}, "westport house upgrade": {"owned": False, "price": 10000}, "main house upgrade": {"owned": False, "price": 20000},
                             "Troost hotel upgrade": {"owned": False, "price": 2000}, "39th hotel upgrade": {"owned": False, "price": 2500}, "Paseo hotel upgrade": {"owned": False, "price": 5000}, "Wornall hotel upgrade": {"owned": False, "price": 10000}, "Roanoke hotel upgrade": {"owned": False, "price": 20000}, "ward hotel upgrade": {"owned": False, "price": 50000}, "westport hotel upgrade": {"owned": False, "price": 100000}, "main hotel upgrade": {"owned": False, "price": 200000}}}
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
    
    