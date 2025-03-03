import sys
input=sys.stdin.readline


k,n=map(int,input().split())
l=[]
for i in range(k):
    l.append(int(input()))

start=1
end=sum(l)//n

while start<=end:
    mid=(start+end)//2
    cnt=[]
    for i in l:
        cnt.append(i//mid)
    cnt_sum=sum(cnt)

    if cnt_sum>=n:
        ans=mid
        start=mid+1
    else:
        end=mid-1


print(ans)
        