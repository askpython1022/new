n, m = map(int,input().split())
basket = [0] * (n+1)
for d in range(m):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        basket[n] = k 

for i in range(1,len(basket)):
    print(basket[i], end = ' ')