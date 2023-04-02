n,m=map(int,input().split())

l = [x for x in range(1, n+1)]

for _ in range(m):
    i, j = map(int,input().split())
    k = l[i-1:j].copy()
    k.reverse()
    l[i-1:j] = k
for i in range(len(l)):
    print(l[i],end=" ")
