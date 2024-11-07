N = int(input())
K = list(map(int, input().split()))

A = []
B = []

K_sort = sorted(K, reverse=True)

A.append(K_sort[0])

for i in range(1, N):
    k = K_sort[i]
    a = sum(A) + k
    b = sum(B) + k

    sum_A = sum(A)
    sum_B = sum(B)

    sabun_p1 = a - sum_B
    sabun_p2 = sum_A - b

    if sabun_p1 > sabun_p2:
        B.append(k)
    else:
        A.append(k)

ans = max(sum(A), sum(B))

print(ans)