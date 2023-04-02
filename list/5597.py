l = [0]*30
for i in range(28):
    a = int(input())
    l[a-1] = 1

for i in range(30):
    if l[i] == 0:
        print(i+1)