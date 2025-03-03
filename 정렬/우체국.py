import sys
input=sys.stdin.readline

n=int(input())
l=[]
mysum=0
for i in range(n):
    a,b=map(int,input().split())
    l.append([a,b])
    mysum+=b
l.sort(key=lambda x: x[0])

ans=0
i=0
cnt=0
while i<len(l):
    cnt+=l[i][1]
    if cnt>=mysum/2:
        print(l[i][0])
        break
    i+=1
