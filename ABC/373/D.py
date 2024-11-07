import numpy as np

N, M = map(int, input().split())

X = [[0]*N for i in range(M)]
y = [0]*M

for i in range(M):
    u, v, w = map(int, input().split())
    X[i][v-1] = 1
    X[i][u-1] = -1
    y[i] = w


rank_X = np.linalg.matrix_rank(A)



print(ans)

