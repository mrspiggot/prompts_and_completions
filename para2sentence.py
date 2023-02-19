import re

def split_into_sentences(text):
    # split the text by end of sentence tokens. '.', '!' & '?'
    sentences = re.split("(?<=[.!?]) +", text)
    return sentences

text = "This is the first sentence. And this, my friends, " \
       "is the second one! Is this the third one? Finally; the end."

sentences = split_into_sentences(text)
print(sentences)
