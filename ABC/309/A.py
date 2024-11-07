A, B = map(int, input().split())

if A + 1 == B:
    if A % 3 != 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")