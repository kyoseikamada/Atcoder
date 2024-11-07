S = input()

T = "BCDEFGHIJKLMNOPQRSTUVWXYZ"

count = 0

pre_index = t_index = S.find("A")

for i in range(len(T)):
    t_index = S.find(T[i])
    idou = abs(pre_index - t_index)
    pre_index = t_index
    count += idou

print(count)