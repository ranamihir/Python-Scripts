def is_prime(x):
    n = 2
    if(x <= 1):
        return False
        
    elif(x == 2):
        return True
        
    else:
        check = True
        while n < x:
            if(x % n == 0):
                check = False
                break
            n += 1
        return check

print is_prime(9)            
print is_prime(101)
print is_prime(100)