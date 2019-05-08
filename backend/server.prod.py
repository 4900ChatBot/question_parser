from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import os
import time 
import json

interpreter = RasaNLUInterpreter('models/current/get_intent')
agent = Agent.load('models/dialogue_chatbot', interpreter=interpreter)

from flask import Flask

app = Flask(__name__, static_url_path='')
@app.route('/api/ask/<question>')
def ask(question):
	responses = agent.handle_message(question)
	return json.dumps(responses)

@app.route('/')
def root():
    return app.send_static_file('index.html')

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)