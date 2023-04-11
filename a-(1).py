#24
N, X = map(int, input().split())

P = list(map(int, input().split()))

result = 0

for i in range(N):
    if P[i] == X:
        result = i + 1

print(result)

#34
