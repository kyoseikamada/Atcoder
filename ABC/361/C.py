N, K = map(int, input().split())
A = list(map(int, input().split()))

sorted_A = sorted(A)

min_A = 10**9

for i in range(K+1):
    x = sorted_A[i+N-K-1] - sorted_A[i]
    if x < min_A:
        min_A = x

print(min_A)