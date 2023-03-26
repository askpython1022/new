X=int(input())
N=int(input())
l=0
for i in range(N):
    a,b=map(int,input().split())
    l=l+(a*b)
if l==X:
    print("Yes")
else:
    print("No")