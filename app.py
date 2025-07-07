from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def bot_reply(message):
    message = message.lower()
    if "halo" in message:
        return "Halo juga! Ada yang bisa saya bantu?"
    elif "siapa kamu" in message:
        return "Saya chatbot sederhana berbasis Python."
    elif "terima kasih" in message:
        return "Sama-sama!"
    else:
        return "Maaf, saya belum mengerti maksud kamu."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    reply = bot_reply(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
