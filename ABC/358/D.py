N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B_sum = sum(B)

N_A = []

for i in range(M):
    find = [A[i] for i in range(N)]

