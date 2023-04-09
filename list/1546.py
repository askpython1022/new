N = int(input())
score= list(map(int,input().split()))
t = max(score)
for i in range(N):
    score[i] = score[i]/t*100
print(sum(score)/N)

