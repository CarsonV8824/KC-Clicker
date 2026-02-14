import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTabWidget, QToolButton, QScrollArea, QSizePolicy, QGridLayout, QMessageBox
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, Signal, Slot

import math

class AchievementsTab(QWidget):
    def __init__(self, game_state:dict) -> None:
        super().__init__()

        self.game_state = game_state
        self.labels:dict[str, QLabel] = {}

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

        for achievement_name in self.game_state['achievements']:
            achievement_label = QLabel(f"{achievement_name}: {'Unlocked' if self.game_state['achievements'][achievement_name] else 'Locked'}")
            achievement_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            scroll_layout.addWidget(achievement_label)

            self.labels[achievement_name] = achievement_label

    def update_achievements(self) -> None:
        for achievement_name in self.game_state['achievements']:
            if not self.game_state['achievements'][achievement_name]:
                if achievement_name == "First Click" and self.game_state["total_clicks"] == 1:
                    
                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the 'First Click' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()
                elif achievement_name == "100 Clicks" and self.game_state["total_clicks"] == 100:
                    
                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the '100 Clicks' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()
                elif achievement_name == "1k Clicks" and self.game_state["total_clicks"] == 1000:
                    
                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the '1k Clicks' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()
                elif achievement_name == "10k Clicks" and self.game_state["total_clicks"] == 10000:
                    
                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the '10k Clicks' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()
                elif achievement_name == "100k Clicks" and self.game_state["total_clicks"] == 100000:
                    
                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the '100k Clicks' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()
                elif achievement_name == "1M Clicks" and self.game_state["total_clicks"] == 1000000:
                    
                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the '1M Clicks' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()
                elif achievement_name == "First Property":
                    for house in self.game_state["houses"]:
                        if self.game_state["houses"][house]["owned"] == 1:
                            
                            msg = QMessageBox(self)
                            msg.setWindowTitle("Achievement Unlocked!")
                            msg.setText("You unlocked the 'First Property' achievement!")
                            msg.setModal(False)  # Non-blocking
                            msg.show()
                            
                            self.game_state['achievements'][achievement_name] = True
                            self.update_labels()
                            break
                elif achievement_name == "5 Properties":
                    total_houses = sum(self.game_state["houses"][house]["owned"] for house in self.game_state["houses"])
                    if total_houses == 5:
                        
                        msg = QMessageBox(self)
                        msg.setWindowTitle("Achievement Unlocked!")
                        msg.setText("You unlocked the '5 Properties' achievement!")
                        msg.setModal(False)  # Non-blocking
                        msg.show()
                        
                        self.game_state['achievements'][achievement_name] = True
                        self.update_labels()
                elif achievement_name == "25 Properties":
                    total_houses = sum(self.game_state["houses"][house]["owned"] for house in self.game_state["houses"])
                    if total_houses == 25:
                        
                        msg = QMessageBox(self)
                        msg.setWindowTitle("Achievement Unlocked!")
                        msg.setText("You unlocked the '25 Properties' achievement!")
                        msg.setModal(False)  # Non-blocking
                        msg.show()
                        
                        self.game_state['achievements'][achievement_name] = True
                        self.update_labels()
                elif achievement_name == "100 Properties":
                    total_houses = sum(self.game_state["houses"][house]["owned"] for house in self.game_state["houses"])
                    if total_houses == 100:
                        
                        msg = QMessageBox(self)
                        msg.setWindowTitle("Achievement Unlocked!")
                        msg.setText("You unlocked the '100 Properties' achievement!")
                        msg.setModal(False)  # Non-blocking
                        msg.show()
                        
                        self.game_state['achievements'][achievement_name] = True
                        self.update_labels()
                elif achievement_name == "500 Properties":
                    total_houses = sum(self.game_state["houses"][house]["owned"] for house in self.game_state["houses"])
                    if total_houses == 500:
                        
                        msg = QMessageBox(self)
                        msg.setWindowTitle("Achievement Unlocked!")
                        msg.setText("You unlocked the '500 Properties' achievement!")
                        msg.setModal(False)  # Non-blocking
                        msg.show()
                        
                        self.game_state['achievements'][achievement_name] = True
                        self.update_labels()
                elif achievement_name == "1k Properties":
                    total_houses = sum(self.game_state["houses"][house]["owned"] for house in self.game_state["houses"])
                    if total_houses == 1000:
                        
                        msg = QMessageBox(self)
                        msg.setWindowTitle("Achievement Unlocked!")
                        msg.setText("You unlocked the '1k Properties' achievement!")
                        msg.setModal(False)  # Non-blocking
                        msg.show()
                        
                        self.game_state['achievements'][achievement_name] = True
                        self.update_labels()
                elif achievement_name == "5k Properties":
                    total_houses = sum(self.game_state["houses"][house]["owned"] for house in self.game_state["houses"])
                    if total_houses == 5000:
                        
                        msg = QMessageBox(self)
                        msg.setWindowTitle("Achievement Unlocked!")
                        msg.setText("You unlocked the '5k Properties' achievement!")
                        msg.setModal(False)  # Non-blocking
                        msg.show()
                        
                        self.game_state['achievements'][achievement_name] = True
                        self.update_labels()
                elif achievement_name == "10k Properties":
                    total_houses = sum(self.game_state["houses"][house]["owned"] for house in self.game_state["houses"])
                    if total_houses == 10000:
                        
                        msg = QMessageBox(self)
                        msg.setWindowTitle("Achievement Unlocked!")
                        msg.setText("You unlocked the '10k Properties' achievement!")
                        msg.setModal(False)  # Non-blocking
                        msg.show()
                        
                        self.game_state['achievements'][achievement_name] = True
                        self.update_labels()
                elif achievement_name == "First Dollar" and self.game_state["total_money"] == 1:
                    
                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the 'First Dollar' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()

                elif achievement_name == "100 Dollars" and self.game_state["total_money"] == 100:
                    
                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the '100 Dollars' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()
                
                elif achievement_name == "1k Dollars" and self.game_state["total_money"] == 1000:
                    
                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the '1k Dollars' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()

                elif achievement_name == "10k Dollars" and self.game_state["total_money"] == 10000:
                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the '10k Dollars' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()

                elif achievement_name == "100k Dollars" and self.game_state["total_money"] == 100000:
                    
                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the '100k Dollars' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()

                elif achievement_name == "1M Dollars" and self.game_state["total_money"] == 1000000:
                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the '1M Dollars' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()

                elif achievement_name == "10M Dollars" and self.game_state["total_money"] == 10000000:

                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the '10M Dollars' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()

                elif achievement_name == "100M Dollars" and self.game_state["total_money"] == 100000000:
                    
                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the '100M Dollars' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()

                elif achievement_name == "1B Dollars" and self.game_state["total_money"] == 1000000000:

                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the '1B Dollars' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()

                elif achievement_name == "10B Dollars" and self.game_state["total_money"] == 10000000000:

                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the '10B Dollars' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()

                elif achievement_name == "100B Dollars" and self.game_state["total_money"] == 100000000000:
                    
                    msg = QMessageBox(self)
                    msg.setWindowTitle("Achievement Unlocked!")
                    msg.setText("You unlocked the '100B Dollars' achievement!")
                    msg.setModal(False)  # Non-blocking
                    msg.show()
                    
                    self.game_state['achievements'][achievement_name] = True
                    self.update_labels()
                

    def update_labels(self) -> None:
        for achievement_name in self.game_state['achievements']:
            self.labels[achievement_name].setText(f"{achievement_name}: {'Unlocked' if self.game_state['achievements'][achievement_name] else 'Locked'}")