import spacy 

nlp =  spacy.load('en_core_web_lg') 

def semantic_score(w1, w2):
    w1 = nlp.vocab[w1]
    w2 = nlp.vocab[w2]

    return (w1.similarity(w2)) * 100 




# ----------------------TESTING -------------------

test_words = [
    ("plane", "plane"),  # Same word, high similarity
    ("car", "automobile"),  # Synonyms, high similarity
    ("happy", "joyful"),  # Synonyms, high similarity
    ("light", "light"),  # Same word, high similarity
    ("dog", "computer"),  # Very different, low similarity
    ("flarn", "blorp")  # Gibberish, very low similarity
]

for word1, word2 in test_words:
    score = semantic_score(word1, word2)
    print(f"Semantic score between '{word1}' and '{word2}': {score:.2f}")
