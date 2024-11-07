N, M = map(int, input().split())
A = list(map(int, input().split()))

jogen_x = max(A)

start_x = jogen_x // 2

max_x = 0

while jogen_x > start_x:
    count = 0
    for a in A:
        count += min(a, start_x)
    
    if count <= M:
        max_x = start_x
        start_x = (start_x + jogen_x) // 2 + 1
    else:
        jogen_x = start_x - 1
        start_x = start_x // 2


if sum(A) <= M:
    print("infinite")
else:
    print(max_x)