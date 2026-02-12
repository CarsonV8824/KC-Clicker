import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTabWidget, QToolButton, QScrollArea, QSizePolicy, QGridLayout
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, Signal, Slot, QTimer

class UpgradesTab(QWidget):
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

        self.add_upgrade_row(scroll_layout, "Upgrade 1", 100)
        self.add_upgrade_row(scroll_layout, "Upgrade 2", 200)

    def add_upgrade_row(self, layout:QVBoxLayout, upgrade_name:str, price:int) -> None:
        row_layout = QHBoxLayout()
        btn = QToolButton()
        
        btn.setIconSize(QSize(125, 125))
        btn.clicked.connect(lambda: self.on_upgrade_click(upgrade_name, price))
        upgrade_label = QLabel(f"Buy {upgrade_name} for ${price}")
        upgrade_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        row_layout.addWidget(btn)
        row_layout.addWidget(upgrade_label)
        layout.addLayout(row_layout)

    def on_upgrade_click(self, upgrade_name:str, price:int) -> None:
        pass
