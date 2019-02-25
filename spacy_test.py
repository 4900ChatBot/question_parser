# What are the requirements for the master's program?
import spacy

# existing model isn't reliable
nlp = spacy.load('en_core_web_sm')
text = (u"What are the requirements for the master's program?")
doc = nlp(text)
for entity in doc.ents:
  print(entity.text, entity.label_)

# similarity isn't reliable either
doc1 = nlp(u"What are the requirements for the master's program?")
doc2 = nlp(u"what is very required for master program?")
similarity = doc1.similarity(doc2)
print(doc1.text, doc2.text, similarity)