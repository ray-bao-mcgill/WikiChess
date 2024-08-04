import spacy
import math 

nlp = spacy.load('en_core_web_lg')  # or 'en_core_web_md'

def semantic_score(w1, w2):
    # replace underscores with spaces if present
    w1 = w1.replace('_', ' ')
    w2 = w2.replace('_', ' ')

    s1 = nlp(w1)
    s2 = nlp(w2)

    similarity = s1.similarity(s2) * 100 
    
    # return as % 
      
    return "{:.1f}".format(similarity)


# ----------------------TESTING -------------------

# test_words = [
#     ("plane", "plane"),  # Same word, high similarity
#     ("car", "automobile"),  # Synonyms, high similarity
#     ("happy", "joyful"),  # Synonyms, high similarity
#     ("light", "light"),  # Same word, high similarity
#     ("dog", "computer"),  # Very different, low similarity
#     ("flarn", "blorp"),  # Gibberish, very low similarity
#     ("Catholic_Church", "Muslim_Church"), # underscore values 
#     ("Ground_fighting", "Catch_wrestling") # underscore values
# ]

# for word1, word2 in test_words:
#     score = semantic_score(word1, word2)
#     print(f"Semantic score between '{word1}' and '{word2}': {score}")