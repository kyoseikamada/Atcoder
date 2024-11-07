from itertools import product

N, K = map(int, input().split())
S = input()

count = 0
S_COUNT = []

for i in range(len(S)-K):
    S_B = S[i:i+K]
    count_hate = S_B.count("?")
    for bit in product((0,1), repeat=count_hate):
        S_B_list = list(S_B)
        k = 0
        for j in range(K):
            if S_B_list[j] == "?":
                if bit[k] == 1:
                    S_B_list[j] = "A"
                    k += 1
                else:
                    S_B_list[j] = "B"
                    k += 1
        
        S_B_str = "".join(S_B_list)

        if S_B_str == S_B_str[::-1]:
            S_COUNT.append(S_B_str)
            count += 1


print(count)