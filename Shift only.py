N = int(input())
a = list(map(int, input().split()))

tick = 0
con = True

while con == True:
    for i in range(N):
         if a[i] % 2 == 0:
             a[i] = a[i]/2
             tick += 1
             print(tick)
             print("the number: ", a[i])
         else:
             con = False
             print(int(tick / N))
             break
    
