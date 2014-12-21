def anti_vowel(text):
    copy = ""
    for letter in text:
        if(letter.lower() != 'a' and letter.lower() != 'e' and letter.lower() != 'i' and letter.lower() != 'o' and letter.lower() != 'u'):
            copy += letter
    return copy
    
print anti_vowel("Mihir")