def median(numbers):
    n = len(numbers)
    mod = sorted(numbers)
    if(n%2 == 0):
        return (float(mod[n/2 - 1]) + float(mod[n/2]))/2
    else:
        return mod[(n - 1)/2]

print median([7,3,1,4])
print median([5,2,3,1,4])