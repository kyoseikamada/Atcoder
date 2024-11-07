import math

N = int(input())

QR = []

for i in range(N):
    q, r = map(int, input().split())
    QR.append((q, r))

Q = int(input())

for i in range(Q):
    t, d = map(int, input().split())
    q, r = QR[t-1]
    k = math.ceil((d-r) / q)
    print(q*k + r)

