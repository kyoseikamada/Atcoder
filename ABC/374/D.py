impot math

N, S, T = map(int, input().split())

hozon = []

for i in range(N):
    a, b, c, d = map(int, input().split())
    hozon.append((a,b,c,d))

saisyo = -1

def kyori(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

tmp = 0
for i in range(N):
    x = kyori(0, 0, hozon[i][0], hozon[i][1])
    if tmp > x:
        saisyo = i

