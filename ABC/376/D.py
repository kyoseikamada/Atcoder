N, M = map(int, input().split())

AB = [[False]*N for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    a = a-1
    b = b-1
    AB[a][b] = True