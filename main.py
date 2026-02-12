from PySide6.QtWidgets import QApplication
import sys

from app.window import MainWindow
from database.db import Database


def load_game_state() -> dict:
    orginal_game_state = {"money": 0, "money_per_second": 0, "Click":1, "houses":{"39th": {"owned":0, "price": 10, "per_second": 1}, "Paseo": {"owned":0, "price": 200, "per_second": 2}, "Wornall": {"owned":0, "price": 300, "per_second": 3}, "Roanoke": {"owned":0, "price": 400, "per_second": 4}},
                "upgrades": {"Clicked":{"owned": False, "price": 50}, "39th house upgrade": {"owned": False, "price": 500}, "Paseo house upgrade": {"owned": False, "price": 1000}, "Wornall house upgrade": {"owned": False, "price": 1500}, "Roanoke house upgrade": {"owned": False, "price": 2000},
                             "39th hotel upgrade": {"owned": False, "price": 2500}, "Paseo hotel upgrade": {"owned": False, "price": 3000}, "Wornall hotel upgrade": {"owned": False, "price": 3500}, "Roanoke hotel upgrade": {"owned": False, "price": 4000}}}
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
    print(game_state)
    app = QApplication(sys.argv)
    window = MainWindow(game_state)

    with open("styles/style.css", "r") as f:
        app.setStyleSheet(f.read())

    window.show()
    return app.exec(), game_state

if __name__ == "__main__":
    game_state = main()[1]
    save_game_state(game_state)
    
    