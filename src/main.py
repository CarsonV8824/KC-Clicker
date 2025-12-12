from flask import Flask, render_template, request, jsonify
from game_logic.game_state import Game_State
from database.database import Database

#---Data Store initilization---#

def load_data_store() -> tuple:
    db = Database()
    data = db.get_data()
    db.close()
    return data

def save_data_store(username: str="test", email: str="test@example.com", stats: dict={}) -> None:
    db = Database()
    db.add_data(username, email, stats)
    db.close()

#---Game State Initialization---#

game_state = Game_State()

#---Biulding Website With Flask---#

app = Flask(__name__)

@app.route('/')
def main():
    try:
        previous_data = load_data_store()
    
        game_state.game_state = previous_data[3]
    except Exception:
        pass
    
    title = "KC-Clicker-Website"
    header = "Welcome to KC-Clicker-Website"
    footer = "© 2025 Carson V"
    
    money = game_state.game_state["money"]
    
    return render_template("index.html", title=title, header=header, footer=footer, money=money)

@app.route('/get_dice_click_from_js', methods=['POST'])
def get_dice_click_from_js():
    
    data = request.get_json()
    
    if data["click"]:
        game_state.game_state["money"] += 1
    
    """with open("tests/test.txt", "a") as f:
        f.write(f"{data}\n")"""
    
    return jsonify({"status": "success", "message": "Dice click received successfully."})

@app.route('/get_dice_info_from_py', methods=['GET'])
def get_dice_info_from_py():
    return jsonify({"count": game_state.game_state["money"], "username": "Player1"})

#---Closing app---#

@app.post("/save-on-close")
def save_on_close():
    
    data = request.get_json(silent=True) or {}

    username = data.get("username", "guest")
    email = data.get("email", "none")
    
    stats = game_state.game_state

    save_data_store(
        username=username,
        email=email,
        stats=stats
    )

    return ("", 204)

#---Running The App---#

if __name__ == '__main__':
    app.run(debug=True)
    