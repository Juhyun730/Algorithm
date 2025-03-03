n,m=map(int,input().split())
l=list(map(int,input().split()))

left = max(l)
right = sum(l)
ans=1e9
while left<=right:
    mid = (left+right)//2
    cnt_sum=0
    count=1
    for i in l:
        if cnt_sum+i>mid:
            count+=1
            cnt_sum=i
        else:
            cnt_sum+=i
    if count<=m:
        if count==m:
            ans=min(ans,mid)
        right=mid-1
    else:
        left=mid+1

print(ans)