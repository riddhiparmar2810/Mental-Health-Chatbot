from chatbot import chatbot


# # Example Flask app configuration
from flask import Flask, render_template

# app = Flask(_name_)

# @app.route('/')
# def index():
#     return render_template('index.html')

from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run()