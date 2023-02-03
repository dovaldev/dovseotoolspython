#import spacy
import difflib

# spacy.cli.download("es_core_news_sm")

# Cargar el modelo de lenguaje de `spacy`
#nlp = spacy.load("es_core_news_sm")


def compare_sentences(sentence1, sentence2):
    # Procesar las frases con `spacy`
    #doc1 = nlp(sentence1)
    #doc2 = nlp(sentence2)
    # Calcular la similitud semántica entre las frases
    #similarity = doc1.similarity(doc2)
    # Imprimir la similitud semántica
    # print("La similitud semántica es:", similarity)
    #return similarity
    pass


def compare_sentences_basic(sentence1, sentence2):
    sentence1 = sentence1.lower()
    sentence2 = sentence2.lower()
    similarity = difflib.SequenceMatcher(None, sentence1, sentence2).ratio()
    return similarity

#print(compare_sentences_basic('1984 de george orwell Manolo pirolo','1984, de George Orwell'))