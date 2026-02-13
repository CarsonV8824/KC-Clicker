import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTabWidget, QToolButton, QScrollArea, QSizePolicy, QGridLayout
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, Signal, Slot, QTimer

from app.houses import HousesTab
from app.upgrades import UpgradesTab
from app.achievements import AchievementsTab
from app.settings import SettingsTab



class MainWindow(QMainWindow):
    
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
        self.button.setIcon(QIcon("images/dollar.png"))
        self.button.setIconSize(QSize(200, 220))
        self.button.setObjectName("click_button")
        self.button.setFixedSize(200, 200)
        
        self.button.clicked.connect(self.handle_click)

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

        # Settings tab
        self.settings_tab = SettingsTab()
        tab.addTab(self.settings_tab, "Settings")
        self.settings_tab.reset_signal.connect(self.reset_game)

        # Passive income timer
        self.income_timer = QTimer()
        self.income_timer.setInterval(1000)  
        self.income_timer.timeout.connect(self.generate_income)
        self.income_timer.start()

    def generate_income(self) -> None:
        if self.game_state["money_per_second"] > 0:
            self.game_state["money"] += 1
            self.income_timer.stop()
            self.income_timer.setInterval(1000/ (self.game_state["money_per_second"]))
            self.income_timer.start()
            self.update_money_labels()

    def handle_click(self) -> None:
        self.game_state["money"] += self.game_state["Click"]
        self.money_label.setText(f"Money: ${self.game_state['money']:,}")

    def update_money_labels(self) -> None:
        self.money_label.setText(f"Money: ${self.game_state['money']:,}")
        self.money_per_second_label.setText(f"Money per second: ${self.game_state['money_per_second']:,}")

    def reset_game(self) -> None:
        self.game_state["money"] = 0
        self.game_state["money_per_second"] = 0
        self.game_state["Click"] = 1
        for house in self.game_state["houses"]:
            self.game_state["houses"][house]["owned"] = 0
            if house == "39th":
                self.game_state["houses"][house]["price"] = 10
                self.game_state["houses"][house]["per_second"] = 1
            elif house == "Paseo":
                self.game_state["houses"][house]["price"] = 200
                self.game_state["houses"][house]["per_second"] = 2
            elif house == "Wornall":
                self.game_state["houses"][house]["price"] = 300
                self.game_state["houses"][house]["per_second"] = 3
            elif house == "Roanoke":
                self.game_state["houses"][house]["price"] = 400
                self.game_state["houses"][house]["per_second"] = 4
        for upgrade in self.game_state["upgrades"]:
            self.game_state["upgrades"][upgrade]["owned"] = False
        self.update_money_labels()
        self.houses_tab.update_labels()
        self.upgrades_tab.update_buttons()