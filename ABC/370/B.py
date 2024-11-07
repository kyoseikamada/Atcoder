N = int(input())

A = []

for i in range(N):
    A.append(list(map(int, input().split())))


ans = 1

for j in range(N):
    if ans >= (j+1):
        ans = A[ans-1][j]
    else:
        ans = A[j][ans-1]

print(ans)