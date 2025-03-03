import sys
input=sys.stdin.readline


k,n=map(int,input().split())
l=[]
for i in range(k):
    l.append(int(input()))

left=1
right=sum(l)//n
ans=0
while left<=right:
    print(left, right)
    mid=(left+right)//2
    cnt=0
    for i in l:
        cnt+=i//mid
    if cnt>=n:
        ans=mid
        left=mid+1
    if cnt<n:
        right=mid-1
        


print(ans)
