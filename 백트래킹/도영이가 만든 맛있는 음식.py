n=int(input())
#신맛은 곱해서 쓴맛은 합해서
l1=[]
l2=[]
for i in range(n):
    s,b=map(int,input().split())
    l1.append(s)
    l2.append(b)

def dfs(i,ss,bb):
    global ans
    for j in range(i,n):
        ss=l1[j]*ss
        bb=l2[j]+bb
        ans=min(ans,abs(ss-bb))
        dfs(j+1,ss,bb)
        ss=int(ss/l1[j])
        bb=int(bb-l2[j])

ans=1e9
for i in range(n):
    ss=l1[i]
    bb=l2[i]
    ans=min(ans,abs(ss-bb))
    dfs(i+1,ss,bb)

print(ans)