m, n = map(int, input().split())
l = []
for i in range(m):
    l.append(i + 1)
for d in range(n):
    i, j=map(int, input().split())
    k = l[j-1]
    l[j-1] = l[i-1]
    l[i-1] = k
for i in range (len(l)):
    print(l[i],end=" ")
