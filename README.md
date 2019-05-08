# question_parser
##### CISC 4900 group project

Chatbot for CIS department undergrad program:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## setup

frontend
```
pushd chatbot_frontend\chatbot-frontend
npm i
popd
```
backend
```
pip install -U rasa_core
pip install rasa_nlu[tensorflow]
python -m rasa_nlu.train -c get_intent_config.yml --data get_intent.md -o models --fixed_model_name get_intent --project current --verbose
python -m rasa_core.train -d domain_chatbot.yml -s stories_chatbot.md -o models/dialogue_chatbot
```
make sure you're running Python 3.6.x
tested on 64bit

## Development
traefik
```
traefik -c serve.toml
```
frontend
```
pushd chatbot_frontend\chatbot-frontend
npm run serve
popd
```
backend
```
python server.py
```

### Trouble shooting
on windows, run the following to set up build tools first if you run into any compile errors when installing any of the above dependencies
```cmd
%comspec% /k "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" amd64 8.1
```
also make sure you're using latest python or else you might get error related to the typing package

### How can I contribute?
```ruby
"R29ldHo0OTAwOzQ5MDBDaGF0Qm90\n"
```