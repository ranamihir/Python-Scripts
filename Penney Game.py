t = int(raw_input())
a = ""
while t:
    num = [0, 0, 0, 0, 0, 0, 0, 0]
    count = int(raw_input())
    a = raw_input()
    for i in range(38):
        if a[i:i + 3] == "TTT":
            num[0] += 1
        elif a[i:i + 3] == "TTH":
            num[1] += 1
        elif a[i:i + 3] == "THT":
            num[2] += 1
        elif a[i:i + 3] == "THH":
            num[3] += 1
        elif a[i:i + 3] == "HTT":
            num[4] += 1
        elif a[i:i + 3] == "HTH":
            num[5] += 1
        elif a[i:i + 3] == "HHT":
            num[6] += 1
        elif a[i:i + 3] == "HHH":
            num[7] += 1
    print count,
    for i in range(7):
         print num[i],
    print num[7]
    t -= 1