N = int(input())
A = list(map(int, input().split()))

A_sorted = sorted(A, reverse=True)
second = A_sorted[1]

second_index = A.index(second)

print(second_index+1)