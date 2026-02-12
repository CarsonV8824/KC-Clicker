import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTabWidget, QToolButton, QScrollArea, QSizePolicy, QGridLayout
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, Signal, Slot, QTimer

from houses import HousesTab

game_state = {"money": 0, "money_per_second": 0, "houses":{"39th": {"owned":0, "price": 10, "per_second": 1}, "Paseo": {"owned":0, "price": 200, "per_second": 2}, "Wornall": {"owned":0, "price": 300, "per_second": 3}, "Roanoke": {"owned":0, "price": 400, "per_second": 4}}}

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("KC Clicker")
        self.resize(420, 240)

        self.count = 0

        self.money_label = QLabel(f"Money: {game_state['money']}")
        self.money_label.setAlignment(Qt.AlignCenter)

        self.money_per_second_label = QLabel(f"Money per second: {game_state['money_per_second']}") 
        self.money_per_second_label.setAlignment(Qt.AlignCenter)
        
        self.button = QPushButton("Click me")
        self.button.clicked.connect(self.handle_click)

        layout = QVBoxLayout()
        layout.addWidget(self.money_label)
        layout.addWidget(self.money_per_second_label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        tab = QTabWidget()
        layout.addWidget(tab)

        # Houses tab

        self.houses_tab = HousesTab(game_state)
        self.houses_tab.purchase_signal.connect(self.update_money_labels)
        tab.addTab(self.houses_tab, "Houses")

        # Passive income timer
        self.income_timer = QTimer()
        self.income_timer.setInterval(1000)  # 1 second
        self.income_timer.timeout.connect(self.generate_income)
        self.income_timer.start()

    def generate_income(self) -> None:
        if game_state["money_per_second"] > 0:
            game_state["money"] += 1
            self.income_timer.stop()
            self.income_timer.setInterval(1000/ (game_state["money_per_second"]))
            self.income_timer.start()
            self.update_money_labels()

    def handle_click(self) -> None:
        game_state["money"] += 1
        self.money_label.setText(f"Money: {game_state['money']}")

    def update_money_labels(self) -> None:
        self.money_label.setText(f"Money: {game_state['money']}")
        self.money_per_second_label.setText(f"Money per second: {game_state['money_per_second']}")


