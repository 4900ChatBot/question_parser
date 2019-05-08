from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import time 
import json

print("Hi! you can ask stuff in this window. Type 'q' to end the conversation.")
print("""
## synonym:compsci
## intent:greet
## intent:bye
## intent:course_list
## intent:info_major
## intent:info_news
## intent:calendar
""")

interpreter = RasaNLUInterpreter('models/current/get_intent')
agent = Agent.load('models/dialogue_chatbot', interpreter=interpreter)

from flask import Flask
app = Flask(__name__)

@app.route('/ask/<question>')
def ask(question):
	responses = agent.handle_message(question)
	return json.dumps(responses)

app.run()
