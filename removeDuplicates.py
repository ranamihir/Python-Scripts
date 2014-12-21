def remove_duplicates(sequence):
    copy = []
    for item in sequence:
            if item not in copy:
                copy.append(item)
    return copy

print remove_duplicates([1,1,2,2,3])