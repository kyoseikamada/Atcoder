N, M = map(int, input().split())
A = list(map(int, input().split()))

jogen_X = M // N

max_x = 0

for i in range(1, jogen_X+1):
    count = 0
    for a in A:
        min_XA = min(i, a)
        count += min_XA

    
    if count <= M:
        if i >= max_x:
            max_x = i
    else:
        break

if sum(A) <= M:
    print("infinite")
else:
    print(max_x)