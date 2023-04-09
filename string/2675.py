a = int(input())
for i in range(a):
    b,B = map(str, input().split())
    for j in range(len(B)):
        print(B[j]*int(b),end='')
    print()

