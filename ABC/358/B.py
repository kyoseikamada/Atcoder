N, A = map(int, input().split())

T = list(map(int, input().split()))

ans = [T[0]+A]

for i in range(1,N):
    if ans[i-1] < T[i]:
        ans.append(T[i]+A)
    else:
        ans.append(ans[i-1]+A)

for i in range(N):
    print(ans[i])