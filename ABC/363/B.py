N, T, P = map(int, input().split())
L = list(map(int, input().split()))

count = 0

while True:
    cn = 0
    for i in range(N):
        if L[i] >= T:
            cn += 1
    
    if cn >= P:
        break
    else:
        count += 1
        for i in range(N):
            L[i] += 1


print(count)