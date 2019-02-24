# question_parser
Experimenting with question parsing implementations
Feel free to add any alternate solutions

### setup
Python 3.7.2

### Spacy
```sh
pip install spacy
python -m spacy download en_core_web_sm
```

### TextBlob
```sh
pip install textblob
python -m textblob.download_corpora
```

### Wit.ai
```sh
pip install wit
```

### Trouble shooting
on windows, run the following to set up build tools first if you run into any compile errors when installing any of the above dependencies
```cmd
%comspec% /k "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" amd64 8.1
```