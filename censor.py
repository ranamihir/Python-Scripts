def censor(text, word):
    s = ""
    for letter in word:
        s += "*"
    copy = text.replace(word, s)
    return copy
    
print censor("What the hell?", "hell")