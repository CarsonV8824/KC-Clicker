import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTabWidget, QToolButton, QScrollArea, QSizePolicy, QGridLayout, QMessageBox
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, Signal, Slot

import math, os

class HousesTab(QWidget):
    purchase_signal = Signal()
    def __init__(self, game_state:dict) -> None:
        super().__init__()
        
        self.game_state = game_state
        self.owned_labels:dict[str, QLabel] = {}
        self.price_labels:dict[str, QLabel] = {}

        self.house_layout = QVBoxLayout()
        self.setLayout(self.house_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.house_layout.addWidget(scroll_area)

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)

        for house_name in self.game_state['houses']:
            print(f"Adding {house_name} row")
            self.add_house_row(scroll_layout, house_name)

    def add_house_row(self, layout:QVBoxLayout, house_name:str) -> None:
        row_layout = QHBoxLayout()
        btn = QToolButton()
        btn.setIcon(QIcon(self.get_image_path(f"{house_name.lower().replace(' ', '_')}.png")))
        btn.setIconSize(QSize(125, 125))
        btn.setFixedSize(150, 150)
        btn.clicked.connect(lambda: self.on_house_click(house_name))
        row_layout.addWidget(btn)

        owned_label = QLabel(f"{house_name}: {self.game_state['houses'][house_name]['owned']:,} owned")
        owned_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        price_label = QLabel(f"Price: ${self.game_state['houses'][house_name]['price']:,}")
        price_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.owned_labels[house_name] = owned_label
        self.price_labels[house_name] = price_label

        row_layout.addWidget(owned_label)
        row_layout.addWidget(price_label)
        layout.addLayout(row_layout)

    def on_house_click(self, house_name:str) -> None:
        if self.game_state["money"] >= self.game_state["houses"][house_name]["price"]:

            if self.game_state["upgrades"]["Per Sec Clicked Bonus"]["owned"]:
                self.game_state["Click"] = sum(math.ceil(self.game_state["houses"][house]["owned"] * self.game_state["houses"][house]["per_second"] * 0.05) for house in self.game_state["houses"])

            self.game_state["money"] -= self.game_state["houses"][house_name]["price"]
            self.game_state["houses"][house_name]["owned"] += 1
            self.game_state["money_per_second"] += self.game_state["houses"][house_name]["per_second"]
            self.game_state["houses"][house_name]["price"] = math.ceil(self.game_state["houses"][house_name]["price"] * 1.15)
            self.update_labels()
            self.purchase_signal.emit()
        else:
            QMessageBox.warning(self, "Not enough money", "You do not have enough money to buy this house.")

    def update_labels(self) -> None:
        for house_name in self.game_state['houses']:
            self.owned_labels[house_name].setText(f"{house_name}: {self.game_state['houses'][house_name]['owned']:,} owned")
            self.price_labels[house_name].setText(f"Price: ${self.game_state['houses'][house_name]['price']:,}")

    @staticmethod
    def get_image_path(image_name: str) -> str:
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, "images", image_name)
        return os.path.join("images", image_name)