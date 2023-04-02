l = [0]*42
for i in range(10):
    a = int(input())
    l[a%42] = 1

cnt = 0
for x in l:
    if x == 1:
        cnt += 1

print(cnt)