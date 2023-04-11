N = int(input())

S = []

first = ['H', 'D', 'C', 'S']
second = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']



result = True

for _ in range(N):
    S.append(input())

S_1 = set(S)
if len(S) != len(S_1):
    result = False

for i in range(N):
    if S[i][0] not in first:
        result = False
        break
    elif S[i][1] not in second:
        result = False
        break

print('Yes' if result else 'No')