N = int(input())
A = []

for i in range(N*N):
    A.append(list(map(int, input().split())))


Q = int(input())
for i in range(Q):
    Lx, Rx, Ly, Ry, Lz, Rz = map(int, input().split())
    ans = 0
    for i in range(Lx, Rx+1):
        for j in range(Ly, Ry+1):
            for k in range(Lz, Rz+1):
                ans += A[(i-1)*N + j - 1][k - 1]

    print(ans)
