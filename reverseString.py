# BETTER(FASTER) WAY:
#def reverse(text):
#    return text[::-1]



# EASIER(SLOWER) WAY:
def reverse(text):
    if len(text) <= 1:
        return text
    else:
        return reverse(text[1:]) + text[0]
    
print reverse("Mihir")