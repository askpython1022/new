H,M = map(int,input().split())
s = int(input())
M=M+s
if M>=60 :
    H = H+1
    M=M-60
    if M>=60 :
        H=H+(M//60)
        M=M-M(M//60)
if H>=24:
    H=H-24
print(H,M)