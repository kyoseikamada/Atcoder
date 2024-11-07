N, Q = map(int, input().split())

left = 1
right = 2

count = 0

for i in range(Q):
    h, t = input().split()
    t = int(t)
    if h == "R":
        k = t - right
        if k < 0:
            k += N
        for j in range(right, right+k):
            if j > N:
                if (j%N) == left:
                    k = N - k
            else:
                if j == left:
                    k = N - k
        count += k
        right = t
    else:
        k = t - left
        if k < 0:
            k += N
        for j in range(left, left+k):
            if j > N:
                if (j%N) == right:
                    k = N - k
            else:
                if j == right:
                    k = N - k
        count += k
        left = t

print(count)

