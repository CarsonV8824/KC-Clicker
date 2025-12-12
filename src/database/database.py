import sqlite3
import json

class Database:
    def __init__(self, db_name='src/database/KC_Clicker.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                Stats TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def add_data(self, username="test", email="test@example.com", stats="{}"):
        self.cursor.execute('''
            INSERT INTO users (username, email, Stats) VALUES (?, ?, ?)
        ''', (username, email, json.dumps(stats)))
        self.connection.commit()

    def get_data(self):
        self.cursor.execute('SELECT * FROM users')
        rows = self.cursor.fetchall()
        for i, row in enumerate(rows):
            user_id, username, email, stats_json = row
            stats = json.loads(stats_json)
            rows[i] = (user_id, username, email, stats)

        rows.reverse()
        return rows[0]

    def close(self):
        self.connection.close()

    def clear_data(self):
        self.cursor.execute('DELETE FROM users')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                Stats TEXT NOT NULL
            )
        ''')
        self.connection.commit()