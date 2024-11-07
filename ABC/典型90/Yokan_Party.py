import itertools

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

Kire = []

for k in list(itertools.combinations(A, K)):
    min_youso = k[0]
    for i in range(len(k)-1):
        if k[i+1] - k[i] < min_youso:
            min_youso = k[i+1] - k[i]
    
    if L - k[len(k)-1] < min_youso:
        min_youso = L - k[len(k)-1]
    
    Kire.append(min_youso)


print(max(Kire))