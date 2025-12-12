from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    title = "KC-Clicker-Website"
    header = "Welcome to KC-Clicker-Website"
    footer = "© 2025 Carson V"
    return render_template("index.html", title=title, header=header, footer=footer)

@app.route('/get_dice_click_from_js', methods=['POST'])
def get_dice_click_from_js():
    data = request.get_json()
    print("Received dice click:", data)
    return jsonify({"status": "success", "message": "Dice click received successfully."})

if __name__ == '__main__':
    app.run(debug=True)