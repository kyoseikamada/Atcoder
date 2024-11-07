N, M = map(int, input().split())

# S = [["."]*N for _ in range(N)]

is_Put = [[False]*N for _ in range(N)]

is_Put_count = N*N

Puts = []

for i in range(M):
    a, b = map(int, input().split())
    # S[a-1][b-1] = "#"
    Puts.append((a-1, b-1))
    is_Put[a-1][b-1] = True
    is_Put_count -= 1

tansaku = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

for i in range(M):
    a, b = Puts[i]

    for k in range(len(tansaku)):
        i, j = tansaku[k]

        a_i = a + i
        b_j = b + j

        if a_i >= 0 and a_i <= N-1 and b_j >= 0 and b_j <= N-1:
            if not is_Put[a_i][b_j]:
                is_Put[a_i][b_j] = True
                is_Put_count -= 1


print(is_Put_count)
