N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_Sorted = sorted(A, reverse=True)
B_Sorted = sorted(B, reverse=True)

total_A = 0
total_B = 0

count = 0

for i in range(N):
    total_A += A_Sorted[i]
    total_B += B_Sorted[i]

    count += 1

    if total_A > X or total_B > Y:
        break


print(count)