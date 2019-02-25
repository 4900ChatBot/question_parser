from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import time

# get started tutorial from official website
interpreter = RasaNLUInterpreter('models/current/nlu')
print("Hi! you can chat in this window. Type 'stop' to end the conversation.")
agent = Agent.load('models/dialogue', interpreter=interpreter)

while True:
    time.sleep(0.3)
    a = input()
    if a == 'stop':
        break
    responses = agent.handle_message(a)
    for r in responses:
        key = 'image' if 'image' in r.keys() else 'text'
        print(r.get(key))
