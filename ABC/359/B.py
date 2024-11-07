N = int(input())
A = list(map(int, input().split()))

count = 0

for i in range(len(A)-2):
    if A[i] == A[i+2]:
        count += 1


print(count)