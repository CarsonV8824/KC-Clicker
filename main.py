from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
import sys, os

from app.window import MainWindow
from database.db import Database
import sys, os

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def main() -> int:
    game_state = Database.load_game_state()
    app = QApplication(sys.argv)
    window = MainWindow(game_state)
    
    css_path = resource_path(os.path.join("styles", "style.css"))
    with open(css_path, "r") as f:
        app.setStyleSheet(f.read())

    app.setApplicationName("KC Clicker")

    icon_path = resource_path(os.path.join("images", "dollar.png"))
    app.setWindowIcon(QIcon(icon_path))

    window.show()
    return app.exec(), game_state

if __name__ == "__main__":
    game_state = main()[1]
    Database.save_game_state(game_state)
    
    