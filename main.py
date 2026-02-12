import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTabWidget, QToolButton, QScrollArea, QSizePolicy, QGridLayout
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize

game_state = {"money": 0, "clicks": 0, "houses":{"39th Street": {"owned":0, "price": 100, "per_second": 1}, "The Paseo": {"owned":0, "price": 200, "per_second": 2}, "Wornall": {"owned":0, "price": 300, "per_second": 3}, "Roanoke": {"owned":0, "price": 400, "per_second": 4}}}

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("KC Clicker")
        self.resize(420, 240)

        self.count = 0

        self.label = QLabel("Button clicked: 0 | Money: 0")
        self.label.setAlignment(Qt.AlignCenter)
        self.button = QPushButton("Click me")
        self.button.clicked.connect(self.handle_click)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        tab = QTabWidget()
        layout.addWidget(tab)

        # Houses tab
        houses_tab = QWidget()
        houses_layout = QVBoxLayout()
        houses_tab.setLayout(houses_layout)
        tab.addTab(houses_tab, "Houses")

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        houses_layout.addWidget(scroll_area)

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)

        def add_house_row(icon_path, house_name):
            row_layout = QHBoxLayout()
            btn = QToolButton()
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(QSize(125, 125))
            btn.setFixedSize(125, 125)
            btn.clicked.connect(lambda: print(f"{house_name} button clicked"))
            row_layout.addWidget(btn)

            owned_label = QLabel(f"{house_name}: {game_state['houses'][house_name]['owned']} owned")
            owned_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            price_label = QLabel(f"Price: ${game_state['houses'][house_name]['price']}")
            price_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            info_layout = QVBoxLayout()
            info_layout.addWidget(owned_label)
            info_layout.addWidget(price_label)
            row_layout.addLayout(info_layout)

            scroll_layout.addLayout(row_layout)

        add_house_row("images/39th.png", "39th Street")
        add_house_row("images/paseo.png", "The Paseo")
        add_house_row("images/wornall.png", "Wornall")
        add_house_row("images/roanoke.png", "Roanoke")

    def handle_click(self) -> None:
        game_state["money"] += 1
        game_state["clicks"] += 1
        self.label.setText(f"Button clicked: {game_state['clicks']} | Money: {game_state['money']}")


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
