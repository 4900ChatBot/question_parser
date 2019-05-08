FROM petronetto/docker-python-deep-learning:latest

RUN rm /etc/apt/sources.list.d/*
RUN apt update
RUN apt-get install -y build-essential gcc make curl
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt install -y nodejs

RUN pip install rasa_core
RUN pip install rasa_nlu[tensorflow]

COPY backend/ chatbot_frontend/ /app/

WORKDIR /app/chatbot-frontend
RUN npm i

WORKDIR /app
RUN python -m rasa_nlu.train -c get_intent_config.yml --data get_intent.md -o models --fixed_model_name get_intent --project current --verbose \
  && python -m rasa_core.train -d domain_chatbot.yml -s stories_chatbot.md -o models/dialogue_chatbot

WORKDIR /app
CMD bash
# docker build -t chatbot .
# docker run -p 3000:3000 -i -t chatbot
