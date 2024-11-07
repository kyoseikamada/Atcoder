from decimal import Decimal
N = int(input())

AB_rate = {}

for i in range(N):
    A, B = map(Decimal, input().split())

    rate = A / (A+B)

    AB_rate[i+1] = rate


rate_sorted = sorted(AB_rate.items(), key=lambda x:x[1], reverse=True)

print(*[x[0] for x in rate_sorted])