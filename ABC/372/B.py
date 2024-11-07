M = int(input())

A = []

m = M

while True:
    for i in range(11):
        if m < 3**i:
            A.append(i-1)
            m = m - 3**(i-1)
            break
        elif m == 3**i:
            A.append(i)
            m = m - 3**i
            break
    if m > 0:
        continue
    else:
        break

print(len(A))
print(*sorted(A))