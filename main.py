from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
import sys, os

from app.window import MainWindow
from database.db import Database
import sys, os

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def get_image_path(image_name: str) -> str:
    if image_name == "style.css":
        return resource_path(os.path.join("styles", "style.css"))
    return resource_path(os.path.join("images", image_name))

def main() -> int:
    game_state = Database.load_game_state()
    app = QApplication(sys.argv)
    window = MainWindow(game_state)

    with open(get_image_path("style.css"), "r") as f:
        app.setStyleSheet(f.read())

    app.setApplicationName("KC Clicker")
    app.setWindowIcon(QIcon(get_image_path("dollar.png")))

    window.show()
    return app.exec(), game_state

if __name__ == "__main__":
    game_state = main()[1]
    Database.save_game_state(game_state)
    
    