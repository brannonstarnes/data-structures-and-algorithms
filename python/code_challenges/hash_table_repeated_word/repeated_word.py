#from hash_table import HashTable
import string

def repeated_word(phrase):
    #for each word in string, hash, add to bucket, value = 1
    # if bucket is not None, return word in string AND word == key.
    # return word

    txt = phrase.translate(str.maketrans("","", string.punctuation))
    word_set = set()
    for word in txt.split():
        word = word.lower()
        if word in word_set:
            return word
        word_set.add(word)

    return None


