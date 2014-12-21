#FASTER WAY:
#def count(sequence, item):
#    return sequence.count(item)
    
#LONGER WAY:
def count(sequence, item):
    s = 0
    for i in sequence:
        if i == item:
            s += 1
    return s
    
print count([1,1,1,2,4,5], 1)