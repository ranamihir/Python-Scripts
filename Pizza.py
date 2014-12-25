def inp():
    x = raw_input()
    if x[0] == '1':
        if x[2] == '2':
            c = 0.5
        else:
            c = 0.25
    else:
        c = 0.75
    return c
def numOfPizzas(portion):
    num = 1
    a = 0
    b = 0
    c = 0
    for i in portion:
        if i == 0.25:
            a += 1
        elif i == 0.5:
            b += 1
        else:
            c += 1
    num += c
    a -= c
    num += (b - b%2)/2
    if b%2 != 0:
        num += 1
        a -=2
    if a > 0:
        num += (a-(a%4))/4
        if a%4>0:
            num += 1
    return num
friends = int(raw_input())
portion = []
while(friends):
    i = inp()
    portion.append(i)
    friends -= 1
print numOfPizzas(portion)
