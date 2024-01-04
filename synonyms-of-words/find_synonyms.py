import nltk
nltk.download('wordnet')
nltk.download('punkt')
from nltk.corpus import wordnet

def get_synonyms(string):
    words = nltk.word_tokenize(string)
    synonyms = set()

    for word in words:
        synonyms.update(get_synonyms_of_word(word))

    return list(synonyms)

def get_synonyms_of_word(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return synonyms

string = "happy beautiful sad"
print(get_synonyms(string))
