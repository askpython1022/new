import sys

for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #",end='')
    print(i+1,end='')
    print(":",end=" ")
    print(a,"+",b,"=",end=" ")
    print(a + b)