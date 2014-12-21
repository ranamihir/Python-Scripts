def purify(sequence):
    copy = []
    i = 0
    while i < len(sequence):
        if sequence[i]%2 == 0:
            copy.append(sequence[i])
        i += 1
    return copy

print purify([1,2,3])