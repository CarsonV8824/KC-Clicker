import sqlite3
import json

class Database:

    def __init__(self, db_file="database/KC-Clicker.db"):
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

    def get_game_state(self):
        self.cursor.execute("SELECT game_state FROM users WHERE id = (SELECT MAX(id) FROM users)")
        result = self.cursor.fetchone()
        return json.loads(result[0]) if result else None
    
    def close(self):
        self.connection.close()

    def __del__(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()