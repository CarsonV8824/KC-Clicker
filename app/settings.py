import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTabWidget, QToolButton, QScrollArea, QSizePolicy, QGridLayout, QMessageBox
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, Signal, Slot

import math

class SettingsTab(QWidget):
    reset_signal = Signal()
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.setLayout(layout)

        reset_button = QPushButton("Reset Game")
        reset_button.setFixedSize(200, 50)
        reset_button.clicked.connect(self.on_reset_click)
        layout.addWidget(reset_button)

    def on_reset_click(self):
        confirm = QMessageBox.question(self, "Confirm Reset", "Are you sure you want to reset your game? This cannot be undone.", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.reset_signal.emit()