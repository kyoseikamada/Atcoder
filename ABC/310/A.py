N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

ans = P

for i in range(N):
    if Q + D[i] <= ans:
        ans = Q + D[i]


print(ans)