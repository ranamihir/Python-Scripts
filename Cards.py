t = int(raw_input())
while(t):
    levels = long(raw_input())
    print int((float(3)*float(levels)*float(levels)/2)+float(levels)/2)%1000007
    t -= 1
