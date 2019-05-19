from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import time 
import json

print("Loaded")

interpreter = RasaNLUInterpreter('models/current/get_intent')
agent = Agent.load('models/dialogue_chatbot', interpreter=interpreter)

from flask import Flask
app = Flask(__name__)

@app.route('/ask/<question>')
def ask(question):
	print(interpreter.parse(question))
	responses = agent.handle_message(question)
	return json.dumps(responses)

app.run()
