H, W = map(int, input().split())
Si, Sj = map(int, input().split())
C = []

for i in range(H):
    C.append(input())

X = input()

H = H-1
W = W-1
Si = Si-1
Sj = Sj-1

for i in range(len(X)):
    if X[i] == "U":
        if Si - 1 >= 0 and C[Si-1][Sj] == ".":
            Si = Si-1
    elif X[i] == "D":
        if Si + 1 <= H and C[Si+1][Sj] == ".":
            Si = Si + 1
    elif X[i] == "L":
        if Sj - 1 >= 0 and C[Si][Sj-1] == ".":
            Sj = Sj - 1
    elif X[i] == "R":
        if Sj + 1 <= W and C[Si][Sj+1] == ".":
            Sj = Sj + 1


print(Si+1, Sj+1)