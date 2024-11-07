N = int(input())
A = list(map(int, input().split()))

count = 0

while True:
    count += 1
    A = sorted(A, reverse=True)
    A[0] -= 1
    A[1] -= 1

    tmp = 0
    for i in A:
        if i >= 1:
            tmp += 1
    
    if tmp <= 1:
        break
    else:
        continue


print(count)