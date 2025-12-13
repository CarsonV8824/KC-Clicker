# Welcome to KC Clicker

## Overview of the Game

A Kansas City Version of Cookie Clicker where you buy locations from Kansas City

## File Overview

- src/
  - database — SQLite storage and access
    - [src/database/KC_Clicker.db](src/database/KC_Clicker.db)
    - [src/database/database.py](src/database/database.py)
  - game_logic — core game state and tick logic
    - [src/game_logic/game_state.py](src/game_logic/game_state.py)
    - [src/game_logic/money_generation.py](src/game_logic/money_generation.py)
  - static — frontend assets served by Flask
    - css: [src/static/css/styles.css](src/static/css/styles.css)
    - images: [src/static/images/39TH_Street.png](src/static/images/39TH_Street.png)
    - js: [src/static/js/script.js](src/static/js/script.js)
  - templates — HTML templates
    - [src/templates/index.html](src/templates/index.html)
  - app entry — Flask server
    - [src/main.py](src/main.py)

- tests/
  - database tests
    - [tests/test_database.py](tests/test_database.py)
