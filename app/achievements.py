import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTabWidget, QToolButton, QScrollArea, QSizePolicy, QGridLayout, QMessageBox
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, Signal, Slot

import math

class AchievementsTab(QWidget):
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