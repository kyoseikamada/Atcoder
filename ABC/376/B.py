N, Q = map(int, input().split())

left = 1
right = 2

count = 0

for i in range(Q):
    h, t = input().split()
    t = int(t)
    if h == "R":
        if t > right and left > right and t > left:
            k = right + N - t
            count += k
        else:
            k = t - right
            if k < 0:
                k += N
            count += k
        right = t
    else:
        if t > left and right > left  and t > right:
            k = left + N - t
            count += k
        else:
            k = t - left
            if k < 0:
                k += N
            count += k
        left = t

print(count)

