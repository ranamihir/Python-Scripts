def pyglatin():
    word = raw_input("Please enter a word: ")
    if(len(word) > 0 and word.isalpha()):
        print word[1:] + word[0] + "ay"
    else:
        print "You did not enter a valid word. Please try again."
        pyglatin()
pyglatin()