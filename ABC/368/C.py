N = int(input())
H = list(map(int, input().split()))

T = 0

for i in range(N):
    h = H[i]
    T_div = (T+1) % 3
    if T_div == 0:
        T += 1
        h -= 3
        if h > 0:
            syou = h // 5
            amari = h % 5

            if amari == 4:
                amari -= 1
            T += (syou*3 + amari)
    elif T_div == 2:
        if h > 1:
            T += 2
            h -= 4
            if h > 0:
                syou = h // 5
                amari = h % 5
                if amari == 4:
                    amari -= 1
                T += (syou*3 + amari)
        else:
            T += 1
    else:
        syou = h // 5
        amari = h % 5
        if amari == 4:
            amari -= 1
        T += (syou*3 + amari)

print(T)