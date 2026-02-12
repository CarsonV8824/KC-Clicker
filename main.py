from PySide6.QtWidgets import QApplication
import sys

from app.window import MainWindow

game_state = {"money": 0, "money_per_second": 0, "houses":{"39th": {"owned":0, "price": 10, "per_second": 1}, "Paseo": {"owned":0, "price": 200, "per_second": 2}, "Wornall": {"owned":0, "price": 300, "per_second": 3}, "Roanoke": {"owned":0, "price": 400, "per_second": 4}}}

def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow(game_state)
    window.show()
    return app.exec()

if __name__ == "__main__":
    raise SystemExit(main())