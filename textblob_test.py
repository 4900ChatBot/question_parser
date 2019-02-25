from textblob import TextBlob

# import nltk
# nltk.download('punkt')
# python -m textblob.download_corpora

text = '''
What are the requirements for the master's program?
'''

# this might be useful for more primitive logics
blob = TextBlob(text)
print(blob.tags)           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

print(blob.noun_phrases)   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])
