N = int(input())
A = list(map(int, input().split()))

ans = []


for i in range(1, N+1):
    ans.append(sum(A[(i-1)*7:i*7]))

print(*ans)