t = int(raw_input())
s = []
br = []
for i in range(t):
    s.append(raw_input())
for i in range(t):
    for j in range(len(s[i])):
        br.append(s[i].index("("))
print br[0]
