FROM python:3.6-slim-stretch

ENV BUILD_PACKAGES="\
        build-essential \
        linux-headers-4.9 \
        python3-dev \
        cmake \
        tcl-dev \
        xz-utils \
        zlib1g-dev \
        git \
        curl \
      	software-properties-common" \
    APT_PACKAGES="\
        ca-certificates \
        openssl \
        graphviz \
        fonts-noto \
        libpng16-16 \
        libfreetype6 \
        libjpeg62-turbo \
        libgomp1 \
        ffmpeg" \
    PIP_PACKAGES="\
        pyyaml \
        mkl \
        cffi \
        h5py \
        requests \
        pillow \
        graphviz \
        numpy \
        pandas \
        scipy \
        scikit-learn \
        seaborn \
        matplotlib \
        jupyter \
        xgboost \
        tensorflow \
        keras \
        torch \
        torchvision \
        rasa_core \
        rasa_nlu[tensorflow] \
        mxnet-mkl" \
    LANG=C.UTF-8
RUN set -ex; \
    rm -rf chatbot_frontend; \
    apt-get update -y; \
    apt-get upgrade -y; \
    apt-get install -y --no-install-recommends ${BUILD_PACKAGES}; \
    apt-get install -y --no-install-recommends ${APT_PACKAGES}; \
    curl -sL https://deb.nodesource.com/setup_8.x | bash -; \
    apt-get install -y nodejs; \
    git clone https://github.com/4900ChatBot/chatbot_frontend.git; \
    cp -r chatbot_frontend/ /app/; \
    pip install -U -v setuptools wheel; \
    pip install -U -v ${PIP_PACKAGES}; \
    apt-get remove --purge --auto-remove -y ${BUILD_PACKAGES}; \
    apt-get clean; \
    apt-get autoclean; \
    apt-get autoremove; \
    rm -rf /tmp/* /var/tmp/*; \
    rm -rf /var/lib/apt/lists/*; \
    rm -rf /var/cache/apt/archives/*.deb \
        /var/cache/apt/archives/partial/*.deb \
        /var/cache/apt/*.bin; \
    find /usr/lib/python3 -name __pycache__ | xargs rm -rf; \
    rm -rf /root/.[acpw]*;
COPY backend/ /app/
WORKDIR /app
RUN python -m rasa_nlu.train -c get_intent_config.yml --data get_intent.md -o models --fixed_model_name get_intent --project current --verbose \
  && python -m rasa_core.train -d domain_chatbot.yml -s stories_chatbot.md -o models/dialogue_chatbot
WORKDIR /app/chatbot-frontend
RUN npm i && npm run build && \
  cp -R build /app/static

WORKDIR /app
CMD python server.prod.py
# docker build -t chatbot .
# docker run -p 5000:5000 -i -t chatbot
