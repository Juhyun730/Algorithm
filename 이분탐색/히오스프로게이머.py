n,k=map(int,input().split())

l=[]
for i in range(n):
    l.append(int(input()))

start=min(l)
end=min(l)+k
ans=0
while end>=start:
    mid=(start+end)//2
    cnt=k
    for i in range(n):
        if l[i]<mid:
            cnt=cnt-(mid-l[i])
            
    if cnt<0:
        end=mid-1
    elif cnt>=0:
        start=mid+1
        ans=max(ans,mid)

print(ans)
    