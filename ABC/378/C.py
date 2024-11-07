N = int(input())
A = list(map(int, input().split()))

B = [-1]

for i in range(1, N):
    a = A[i]
    find = False
    for j in range(i-1, -1, -1):
        if a == A[j]:
            B.append(j+1)
            find = True
            break
    if not find:
        B.append(-1)

print(*B)