a = []
def minMoves(packets, candies):
    c = 0
    moves = 0
    for i in candies:
        c += i
    if c%packets != 0:
        moves = -1
    else:
        e = c/packets
        for candy in candies:
            if candy < e:
                moves += (e-candy)
    return moves
candies = []
while(1):
    packets = int(raw_input())
    if packets == -1:
        break;
    else:
        for i in range(packets):
            x = int(raw_input())
            candies.append(x)
        print minMoves(packets, candies)
        candies = []
