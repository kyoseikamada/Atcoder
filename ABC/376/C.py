N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sort = sorted(A, reverse=True)
B_sort = sorted(B, reverse=True)

ans = A_sort[N-1]
k = 0
j = 0

for i in range(N):
    if B_sort[j] >= A_sort[i]:
        j += 1
        if j == N-1:
            break
    else:
        ans = A_sort[i]
        k += 1
        if k >= 2:
            ans = -1
            break

print(ans)

