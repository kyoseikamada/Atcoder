N = int(input())

A = []

for i in range(N):
    A.append(list(map(int, input())))

ans = [[0]*N for i in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0:
            if j == N-1:
                ans[i+1][j] = A[i][j]
            else:
                ans[i][j+1] = A[i][j]
        elif i == N-1:
            if j == 0:
                ans[i-1][j] = A[i][j]
            else:
                ans[i][j-1] = A[i][j]
        else:
            if j == 0:
                ans[i-1][j] = A[i][j]
            elif j == N-1:
                ans[i+1][j] = A[i][j]
            else:
                ans[i][j] = A[i][j]

for i in range(N):
    print(*ans[i], sep="")