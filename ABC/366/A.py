N, T, A = map(int, input().split())

if T == A:
    print("No")
else:
    if T > A:
        sabun = T - A
        if sabun > N - T - A:
            print("Yes")
        else:
            print("No")
    elif T < A:
        sabun = A - T
        if sabun > N - T - A:
            print("Yes")
        else:
            print("No")