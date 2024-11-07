A = list(map(int, input().split()))

count = 0

index = 0

while len(A) > 0:
    a = A.pop(index)
    for i in range(len(A)):
        if A[i] == a:
            count += 1
            A.pop(i)
            break

print(count)
