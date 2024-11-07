
N, M = map(int, input().split())

X = [0]*N
X_Flag = [False]*N

F = [[0]*N for i in range(N)]

for i in range(M):
    u, v, w = map(int, input().split())
    F[u-1][v-1] = 1
    F[v-1][u-1] = 1
    if not X_Flag[u-1] and not X_Flag[v-1]:
        X[u-1] = w
        X[v-1] = w + X[u-1]
        X_Flag[u-1] = True
        X_Flag[v-1] = True
    elif not X_Flag[u-1] and X_Flag[v-1]:
        X[u-1] = X[v-1] - w
        X_Flag[u-1] = True
    elif X_Flag[u-1] and not X_Flag[v-1]:
        X[v-1] = w + X[u-1]
        X_Flag[v-1] = True
    else:
        k = X[v-1] - X[u-1]

        if k == w:
            continue
        else:
            if w > k:
                zan = w - k
                X[v-1] += zan
                for i in range(N)
        

print(*X)

