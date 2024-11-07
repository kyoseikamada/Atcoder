A, B, C = map(int, input().split())

ans = True

if B > C:
    for i in range(B, B+(24-B)+C):
        if i >= 24:
            if i % 12 == A:
                ans = False
                break
        else:
            if i == A:
                ans = False
                break

    if ans:
        print("Yes")
    else:
        print("No")
else:
    if B == C:
        print("Yes")
    else:
        for i in range(B, C):
            if i == A:
                ans = False
                break

        if ans:
            print("Yes")
        else:
            print("No")