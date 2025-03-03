import sys
input=sys.stdin.readline

n,k=map(int,input().split())
sl=[]
for i in range(n):
    sl.append(input().strip())

if k<=4:
    print(0)
    exit(0)

l={'a','n','t','i','c'}
visited=[0]*26

for i in l:
    visited[ord(i)-97]=1

ans=0
def canread(s):
    flag=True
    for idx in s:
        if visited[ord(idx)-97]==0:
            flag=False
            break
    return flag

def dfs(start):
    global ans

    if sum(visited)==k:
        cnt=0
        for x in sl:
            if canread(x):
                cnt+=1
        ans=max(ans,cnt)
        return
    else:
        for alpha in range(start,26):
            if visited[alpha]==0:
                visited[alpha]=1
                dfs(alpha+1)
                visited[alpha]=0

dfs(0)
print(ans)
