import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTabWidget, QToolButton, QScrollArea, QSizePolicy, QGridLayout, QToolTip, QMessageBox
from PySide6.QtGui import QIcon, QPixmap, QCursor
from PySide6.QtCore import Qt, QSize, Signal, Slot, QTimer, QPoint, QRect

from app.houses import HousesTab
from app.upgrades import UpgradesTab
from app.achievements import AchievementsTab
from app.settings import SettingsTab

from database.db import Database

import os
import time

class MainWindow(QMainWindow):
    achievement_signal = Signal()
    def __init__(self, game_state:dict) -> None:
        super().__init__()
        self.setWindowTitle("KC Clicker")
        self.resize(450, 600)

        self.game_state = game_state

        self.money_label = QLabel(f"Money: ${self.game_state['money']:,}")
        self.money_label.setAlignment(Qt.AlignCenter)

        self.money_per_second_label = QLabel(f"Money per second: ${self.game_state['money_per_second']:,}") 
        self.money_per_second_label.setAlignment(Qt.AlignCenter)
        

        self.button = QPushButton()
        self.button.setIcon(QIcon(self.get_image_path("dollar.png")))
        self.button.setIconSize(QSize(200, 220))
        self.button.setObjectName("click_button")
        self.button.setFixedSize(200, 200)
        
        self.button.mousePressEvent = self.handle_click

        button_container = QWidget()
        button_layout = QHBoxLayout(button_container)
        button_layout.addWidget(self.button)

        layout = QVBoxLayout()
        layout.addWidget(self.money_label)
        layout.addWidget(self.money_per_second_label)
        layout.addWidget(button_container)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        tab = QTabWidget()
        layout.addWidget(tab)

        # Houses tab

        self.houses_tab = HousesTab(self.game_state)
        self.houses_tab.purchase_signal.connect(self.update_money_labels)
        tab.addTab(self.houses_tab, "Houses")

        # Upgrades tab
        self.upgrades_tab = UpgradesTab(self.game_state)
        tab.addTab(self.upgrades_tab, "Upgrades")
        self.upgrades_tab.upgrade_signal.connect(self.update_money_labels)

        # Achievements tab
        self.achievements_tab = AchievementsTab(self.game_state)
        tab.addTab(self.achievements_tab, "Achievements")
        self.upgrades_tab.upgrade_signal.connect(self.achievement_signal)
        self.houses_tab.purchase_signal.connect(self.achievement_signal)
        self.achievement_signal.connect(self.achievements_tab.update_achievements)

        # Settings tab
        self.settings_tab = SettingsTab()
        tab.addTab(self.settings_tab, "Settings")
        self.settings_tab.reset_signal.connect(self.reset_game)

        # Passive income timer
        self.income_timer = QTimer()
        self.income_timer.setInterval(50)
        self.income_timer.timeout.connect(self.generate_income)
        self._last_income_time = time.perf_counter()
        self._pending_income = 0.0
        self.income_timer.start()

    def generate_income(self) -> None:
        now = time.perf_counter()
        elapsed_seconds = now - self._last_income_time
        self._last_income_time = now

        money_per_second = self.game_state["money_per_second"]
        if money_per_second <= 0:
            return

        self._pending_income += elapsed_seconds * money_per_second
        income_to_add = int(self._pending_income)
        if income_to_add <= 0:
            return

        self._pending_income -= income_to_add
        self.achievement_signal.emit()
        self.game_state["money"] += income_to_add
        self.game_state["total_money"] += income_to_add
        self.update_money_labels()

    def handle_click(self, event) -> None:
        self.game_state["total_clicks"] += 1
        self.achievement_signal.emit()
        self.game_state["money"] += self.game_state["Click"]
        self.game_state["total_money"] += self.game_state["Click"]
        self.money_label.setText(f"Money: ${self.game_state['money']:,}")

        text = f"+${self.game_state['Click']:,}"

        # show tooltip exactly where the user clicked
        click_global = event.globalPosition().toPoint()  # PySide6
        QToolTip.showText(click_global, text, self.button, self.button.rect(), 1500)
        # keep normal button behavior
        self.button.click()
        

    def update_money_labels(self) -> None:
        self.achievement_signal.emit()
        self.money_label.setText(f"Money: ${self.game_state['money']:,}")
        self.money_per_second_label.setText(f"Money per second: ${self.game_state['money_per_second']:,}")

    def reset_game(self) -> None:
        default_game_state = Database.reset_db()
        self.game_state.clear()
        self.game_state.update(default_game_state)

        self.update_money_labels()
        self.houses_tab.update_labels()
        self.upgrades_tab.update_buttons()
        self.achievement_signal.emit()

    @staticmethod
    def get_image_path(image_name: str) -> str:
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, "images", image_name)
        return os.path.join("images", image_name)
