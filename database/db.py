import sqlite3
import json
import os
import sys

from database.game_state import game_state

class Database:

    def __init__(self):
        db_file=self.get_db_path()
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.__make_table()
    
    def __make_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                game_state TEXT NOT NULL
                )""")
        
    def add_game_state(self, game_state):
        self.cursor.execute("INSERT INTO users (game_state) VALUES (?)", (json.dumps(game_state),))
        self.connection.commit()

    def get_game_state(self) -> dict:
        self.cursor.execute("SELECT game_state FROM users WHERE id = (SELECT MAX(id) FROM users)")
        result = self.cursor.fetchone()
        return json.loads(result[0]) if result else None
    
    def delete_game_state(self) -> None:
        self.cursor.execute("DELETE FROM users")
        self.connection.commit()
    
    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    @staticmethod
    def get_db_path() -> str:
        if hasattr(sys, '_MEIPASS'):
            # Save to user's app data folder so it persists
            app_data = os.path.join(os.path.expanduser("~"), "KC-Clicker")
            os.makedirs(app_data, exist_ok=True)
            return os.path.join(app_data, "KC-Clicker.db")
        return os.path.join(os.path.dirname(__file__), "KC-Clicker.db")
    
    @staticmethod
    def reset_db() -> dict:
        os.remove(Database.get_db_path())
        return game_state()

    @staticmethod
    def load_game_state() -> dict:
        loaded_game_state = game_state()
        try:
            with Database() as db:
                data = db.get_game_state()
                if data:
                    loaded_game_state.update(data)
                    return loaded_game_state
                else:
                    return loaded_game_state
        except Exception as e:
            print(f"Error loading game state: {e}")
            return loaded_game_state
        
    @staticmethod
    def save_game_state(game_state: dict) -> None:
        with Database() as db:
            db.add_game_state(game_state)