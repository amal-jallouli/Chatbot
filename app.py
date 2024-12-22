from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Set up the chatbot
chatbot = ChatBot('ChatterBot', storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[
                      'chatterbot.logic.BestMatch',
                      'chatterbot.logic.MathematicalEvaluation',
                      'chatterbot.logic.TimeLogicAdapter'
                  ],
                  database_uri='sqlite:///database.db')

# Train the chatbot using the ChatterBot corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

# Route to render the frontend (HTML page)
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle user input and provide chatbot responses
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    bot_response = chatbot.get_response(user_input)
    return jsonify({'response': str(bot_response)})

if __name__ == '__main__':
    app.run(debug=True)
