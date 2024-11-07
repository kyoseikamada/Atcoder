import math

N = int(input())

ans = 0

def cost(x1, y1, x2, y2):
    x = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return x

now_x = 0
now_y = 0

for i in range(N):
    x1, y1 = map(int, input().split())

    tmp = cost(now_x, now_y, x1, y1)

    ans += tmp

    now_x = x1
    now_y = y1


ans += cost(now_x, now_y, 0, 0)

print(ans)

