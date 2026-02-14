import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTabWidget, QToolButton, QScrollArea, QSizePolicy, QGridLayout, QMessageBox
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, Signal, Slot, QTimer

import math, os

class UpgradesTab(QWidget):
    upgrade_signal = Signal()
    def __init__(self, game_state:dict) -> None:
        super().__init__()

        self.game_state = game_state

        self.upgrades:dict[str, QToolButton] = {}

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.setLayout(layout)
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)

        for upgrade_name in self.game_state['upgrades']:
            print(f"Adding {upgrade_name} row")
            self.add_upgrade_row(scroll_layout, upgrade_name, self.game_state['upgrades'][upgrade_name]['price'])

        self.update_buttons()

    def add_upgrade_row(self, layout:QVBoxLayout, upgrade_name:str, price:int) -> None:
        row_layout = QHBoxLayout()
        btn = QToolButton()
        if upgrade_name.count("house") > 0 or upgrade_name.count("House") > 0:
            btn.setIcon(QIcon(self.get_image_path("house.png")))
            btn.setIconSize(QSize(125, 125))
        elif upgrade_name.count("hotel") > 0 or upgrade_name.count("Hotel") > 0:
            btn.setIcon(QIcon(self.get_image_path("hotel.png")))
            btn.setIconSize(QSize(125, 125))
        elif upgrade_name.count("Clicked") > 0:
            btn.setIcon(QIcon(self.get_image_path("clicker.png")))
            btn.setIconSize(QSize(125, 125))
        btn.setFixedSize(150, 150)
        btn.clicked.connect(lambda: self.on_upgrade_click(upgrade_name, price))
        upgrade_label = QLabel(f"Buy {upgrade_name} for ${price:,}")
        upgrade_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        row_layout.addWidget(btn)
        row_layout.addWidget(upgrade_label)
        layout.addLayout(row_layout)

        self.upgrades[upgrade_name] = btn

    def on_upgrade_click(self, upgrade_name:str, price:int) -> None:
        if self.game_state["money"] >= price and not self.game_state["upgrades"][upgrade_name]["owned"]:
            
            if upgrade_name == "Clicked":
                self.game_state["money"] -= price
                self.game_state["upgrades"][upgrade_name]["owned"] = True
                self.game_state["Click"] += 1
                self.upgrades[upgrade_name].setEnabled(False)
                self.upgrade_signal.emit()
                return
            elif upgrade_name == "Per Sec Clicked Bonus":
                self.game_state["money"] -= price
                self.game_state["upgrades"][upgrade_name]["owned"] = True
                self.game_state["Click"] += sum(math.ceil(self.game_state["houses"][house]["owned"] * self.game_state["houses"][house]["per_second"] * 0.05) for house in self.game_state["houses"])
                self.upgrades[upgrade_name].setEnabled(False)
            else:
                self.game_state["money"] -= price
                self.game_state["upgrades"][upgrade_name]["owned"] = True
                self.game_state["houses"][upgrade_name.split()[0]]["per_second"] *= 2
                self.game_state["money_per_second"] += self.game_state["houses"][upgrade_name.split()[0]]["owned"] * self.game_state["houses"][upgrade_name.split()[0]]["per_second"] // 2

                if self.game_state["upgrades"]["Per Sec Clicked Bonus"]["owned"]:
                    self.game_state["Click"] = sum(math.ceil(self.game_state["houses"][house]["owned"] * self.game_state["houses"][house]["per_second"] * 0.05) for house in self.game_state["houses"])

                self.upgrades[upgrade_name].setEnabled(False)
                self.upgrade_signal.emit()
                return

        elif self.game_state["money"] < price:
            QMessageBox.warning(self, "Not enough money", "You do not have enough money to buy this upgrade.")

    def update_buttons(self) -> None:
        for upgrade_name in self.game_state['upgrades']:
            if self.game_state["upgrades"][upgrade_name]["owned"]:
                self.upgrades[upgrade_name].setEnabled(False)
            else:
                self.upgrades[upgrade_name].setEnabled(True)

    @staticmethod
    def get_image_path(image_name:str) -> str:
        return os.path.join("images", image_name)
            
                
