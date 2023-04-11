from collections import Counter

N = int(input())
A = list(map(int, input().split()))

C = Counter(A)

ans = 0

for c in C:
    ans += C[c]//2


print(ans)
