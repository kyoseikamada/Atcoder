N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))

zero = []
one = []

for i in range(N):
    if S[i] == "0":
        zero.append(X[i])
    else:
        one.append(X[i])

count = 0

for i in range(len(zero)):
    for j in range(len(one)):
        z = zero[i]
        o = one[j]
        if z < o:
             next
        else:
            if (abs(o-z) / 2) <= T + 0.1:
                count += 1
        

print(count)