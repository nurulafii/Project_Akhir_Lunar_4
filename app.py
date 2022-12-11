from chat_me import preparation, generate_response
from flask import Flask, render_template, request
# from audio import *

# download nltk
preparation()

#Start Chatbot
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    result = generate_response(user_input)
    return result
# @app.route("/record")
# def record():
#     text = dengerin()
#     # result = generate_response(text)
#     # bilang(text)
#     return text

# @app.route("/speak")
# def speak():
#     user_input = str(request.args.get('msg'))
#     bilang(user_input)
    
if __name__ == "__main__":
    app.run(debug=True)