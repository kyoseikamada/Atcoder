N = int(input())
K = list(map(int, input().split()))

A = []
B = []

K_sort = sorted(K, reverse=True)

koho = []

def furiwake(A:list, B:list, index):

    if index == N:
        koho.append(max(sum(A), sum(B)))
        return

    new_A = A.copy()
    new_A.append(K[index])
    new_B = B.copy()
    new_B.append(K[index])
    furiwake(new_A, B, index+1)
    furiwake(A, new_B, index+1)

furiwake(A, B, 0)

print(min(koho))