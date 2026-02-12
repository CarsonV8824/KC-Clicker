import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTabWidget, QToolButton, QScrollArea, QSizePolicy, QGridLayout
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, Signal, Slot, QTimer

class UpgradesTab(QWidget):
    upgrade_signal = Signal()
    def __init__(self, game_state:dict) -> None:
        super().__init__()

        self.game_state = game_state

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

    def add_upgrade_row(self, layout:QVBoxLayout, upgrade_name:str, price:int) -> None:
        row_layout = QHBoxLayout()
        btn = QToolButton()
        if upgrade_name.count("house" or "House") > 0:
            btn.setIcon(QIcon(f"images/house.png"))
            btn.setIconSize(QSize(125, 125))
        elif upgrade_name.count("hotel" or "Hotel") > 0:
            btn.setIcon(QIcon(f"images/hotel.png"))
            btn.setIconSize(QSize(125, 125))
        btn.setFixedSize(125, 125)
        btn.clicked.connect(lambda: self.on_upgrade_click(upgrade_name, price))
        upgrade_label = QLabel(f"Buy {upgrade_name} for ${price}")
        upgrade_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        row_layout.addWidget(btn)
        row_layout.addWidget(upgrade_label)
        layout.addLayout(row_layout)

    def on_upgrade_click(self, upgrade_name:str, price:int) -> None:
        if self.game_state["money"] >= price and not self.game_state["upgrades"][upgrade_name]["owned"]:
            
            if upgrade_name == "Clicked":
                self.game_state["money"] -= price
                self.game_state["upgrades"][upgrade_name]["owned"] = True
                self.game_state["Click"] *= 2
                self.upgrade_signal.emit()
            else:
                self.game_state["money"] -= price
                self.game_state["upgrades"][upgrade_name]["owned"] = True
                self.game_state["houses"][upgrade_name.split()[0]]["per_second"] *= 2
                self.game_state["money_per_second"] += self.game_state["houses"][upgrade_name.split()[0]]["owned"] * self.game_state["houses"][upgrade_name.split()[0]]["per_second"] // 2
                self.upgrade_signal.emit()
            
                
