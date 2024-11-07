N = int(input())
A = []
TMP = []


for i in range(N):
    a = input()
    A.append(a)
    TMP.append(a)


for i in range(N//2):
    for j in range(i, N-i):
        for k in range(i, N-i):
            A[k] = TMP[k][:N-j-2] + TMP[j][k] + TMP[k][N-j-1:]

    TMP = A.copy()


for i in range(N):
    print(A[i])