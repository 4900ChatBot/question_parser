from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import time

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

# interpreter = RasaNLUInterpreter('models/current/nlu')
# agent = Agent.load('models/dialogue', interpreter=interpreter)

interpreter = RasaNLUInterpreter('models/current/get_intent')
agent = Agent.load('models/dialogue_chatbot', interpreter=interpreter)

while True:
    time.sleep(0.3)
    msg = input()
    if msg == 'q':
        break
    # print(interpreter.parse(msg))
    responses = agent.handle_message(msg)
    print(responses)
    # for r in responses:
    #     key = 'image' if 'image' in r.keys() else 'text'
    #     print(r.get(key))
