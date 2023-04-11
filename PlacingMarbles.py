
zero_one = input()

count = 0

for i in range(3):
    if zero_one[i] == "1":
        count += 1
print(count)
print(type(zero_one))