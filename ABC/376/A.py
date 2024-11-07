N, C = map(int, input().split())
T = list(map(int, input().split()))

count = 1
zenkai = T[0]

for i in range(1, N):
    if T[i] - zenkai < C:
        continue
    else:
        count += 1
        zenkai = T[i]

print(count)