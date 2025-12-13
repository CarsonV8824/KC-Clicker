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
    thirty_nine_street_button = "39th Street owned: " + str(game_state.game_state["producers"]["39th street owned"]) + " | Cost: " + str(game_state.game_state["producers"]["cost"])
    
    money = game_state.game_state["money"]
    money_per_sec = game_state.game_state["money_per_sec"]
    
    return render_template("index.html", title=title, header=header, footer=footer, money=money, money_per_sec=money_per_sec, thirty_nine_street_button=thirty_nine_street_button)

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
    return jsonify({"count": game_state.game_state["money"], "username": game_state.game_state["username"]})

@app.route('/get_39th_street_button_click_from_js', methods=['POST'])
def get_39th_street_button_click_from_js():
    
    data = request.get_json()
    
    cost = game_state.game_state["producers"]["39th_street"]["cost"]
    
    if data["buy"]:
        if game_state.game_state["money"] >= cost:
            game_state.game_state["money"] -= cost
            game_state.game_state["producers"]["39th_street"]["owned"] += 1
            game_state.game_state["producers"]["39th_street"]["$PerSec"] += 1
            game_state.game_state["money_per_sec"] += 1
            game_state.game_state["producers"]["39th_street"]["cost"] = int(cost * 1.15)
    
    return jsonify({"status": "success", "message": "39th Street button click received successfully."})

@app.route('/get_money_per_sec_info_from_py', methods=['GET'])
def get_money_per_sec_info_from_py():
    return jsonify({"money_per_sec": game_state.game_state["money_per_sec"]})

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
    