n = int(input())
m = n // 4
if n % 4 != 0: m += 1
for _ in range(m):
    print("long",end=" ")
print("int")