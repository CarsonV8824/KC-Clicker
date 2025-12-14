from flask import Flask, render_template, request, jsonify
from game_logic.game_state import Game_State
from game_logic.money_generation import Money_Generation
from database.database import Database

import json

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
        game_state.game_state = game_state.default_game_state()

    title = "KC-Clicker-Website"
    header = "Welcome to KC-Clicker-Website"
    footer = "© 2025 Carson V"

    thirty_nine_street_producer = game_state.game_state["producers"]["39th_street"]
    thirty_nine_street_owned = thirty_nine_street_producer.get("owned", 0)
    thirty_nine_street_button = thirty_nine_street_producer["cost"]
    thirty_nine_street_button = f"39th Street owned: {thirty_nine_street_owned} | Cost: {thirty_nine_street_button}"

    the_paseo_producer = game_state.game_state["producers"]["The_Paseo"]
    the_paseo_owned = the_paseo_producer.get("owned", 0)
    the_paseo_button = the_paseo_producer["cost"]
    the_paseo_button = f"The Paseo owned: {the_paseo_owned} | Cost: {the_paseo_button}"


    money = game_state.game_state["money"]
    money_per_sec = game_state.game_state["money_per_sec"]

    return render_template(
        "index.html",
        title=title,
        header=header,
        footer=footer,
        money=money,
        money_per_sec=money_per_sec,
        thirty_nine_street_button=thirty_nine_street_button,
        the_paseo_button=the_paseo_button
    )

#---Dice Click Info---#

@app.route('/get_dice_click_from_js', methods=['POST'])
def get_dice_click_from_js():
    data = request.get_json(silent=True) or {}
    if data.get("click"):
        game_state.game_state["money"] += 1
    return jsonify({"status": "success", "message": "Dice click received successfully."})

@app.route('/get_dice_info_from_py', methods=['GET'])
def get_dice_info_from_py():
    username = game_state.game_state.get("username", "guest")
    return jsonify({"count": game_state.game_state["money"], "username": username})

#---39th Street Button Click Info---#

@app.route('/get_39th_street_button_click_from_js', methods=['POST'])
def get_39th_street_button_click_from_js():
    data = request.get_json(silent=True) or {}
    cost = game_state.game_state["producers"]["39th_street"]["cost"]

    if data.get("buy") and game_state.game_state["money"] >= cost:
        game_state.game_state["money"] -= cost
        # Update producer stats consistently
        producer = game_state.game_state["producers"]["39th_street"]
        producer["owned"] = producer.get("owned", 0) + 1
        producer["per_sec"] = producer.get("per_sec", 0) + 1
        # Recompute money_per_sec from producers or increment directly
        game_state.game_state["money_per_sec"] += game_state.game_state["producers"]["39th_street"]["$PerSec"]
        producer["cost"] = int(round((cost * 1.15)))

    return jsonify({"status": "success", "message": "39th Street button click received successfully."})

@app.route("/get_39th_street_button_click_from_py")
def get_39th_street_button_click_from_py():
    producer = game_state.game_state["producers"]["39th_street"]
    return jsonify({
        "owned": producer.get("owned", 0),
        "cost": producer["cost"]
    })

#---The Paseo Button Click Info---#

@app.route('/get_The_Paseo_button_click_from_js', methods=['POST'])
def get_The_Paseo_button_click_from_js():
    data = request.get_json(silent=True) or {}
    cost = game_state.game_state["producers"]["The_Paseo"]["cost"]

    if data.get("buy") and game_state.game_state["money"] >= cost:
        game_state.game_state["money"] -= cost
        # Update producer stats consistently
        producer = game_state.game_state["producers"]["The_Paseo"]
        producer["owned"] = producer.get("owned", 0) + 1
        producer["per_sec"] = producer.get("per_sec", 0) + 5
        # Recompute money_per_sec from producers or increment directly
        game_state.game_state["money_per_sec"] += game_state.game_state["producers"]["The_Paseo"]["$PerSec"]
        producer["cost"] = int(round((cost * 1.15)))

    return jsonify({"status": "success", "message": "The Paseo button click received successfully."})

@app.route("/get_The_Paseo_button_click_from_py")
def get_The_Paseo_button_click_from_py():
    producer = game_state.game_state["producers"]["The_Paseo"]
    return jsonify({
        "owned": producer.get("owned", 0),
        "cost": producer["cost"]
    })

#---Money Per Sec Info---#

@app.route('/get_money_per_sec_info_from_py', methods=['GET'])
def get_money_per_sec_info_from_py():
    return jsonify({"money_per_sec": game_state.game_state["money_per_sec"]})

#---Money Generation Thread---#

money_generation = Money_Generation(game_state)

@app.route('/get_money_generation_from_py', methods=['GET'])
def get_money_generation_from_py():
    return jsonify({"money": game_state.game_state["money"]})

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

    #--testing json dump--#
    """
    with open("tests/test.json", "a") as f:
        json.dump((game_state.game_state), f)
    """
        
    return ("", 204)

#---Running The App---#

if __name__ == '__main__':
    app.run(debug=True)
    