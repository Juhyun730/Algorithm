import sys
input=sys.stdin.readline
d=int(input())
ans=[]

for i in range(d):
    n=int(input())
    l=list(map(int,input().split()))
    mysum=0
    mymax=l[-1]
    for k in range(n-2,-1,-1):
        if mymax<l[k]:
            mymax=l[k]
        mysum+=mymax-l[k]
    ans.append(mysum)

for i in ans:
    print(i)


