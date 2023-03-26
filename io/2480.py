A,B,C=map(int,input().split())
if A==B==C:
    print(10000+1000*A)
elif A==C:
    print(1000+A*100)
elif A==B:
    print(1000+A*100)
elif C==B:
    print(1000+C*100)
else:
    if A<B:
        if B<C:
            print(C*100)
        else :
            print(B*100)
    elif A<C:
        if C<B:
            print(B*100)
        else:
            print(C*100)
    else:
        print(A*100)

