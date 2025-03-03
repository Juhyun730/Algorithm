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
    visited[ord(i)-ord('a')]=1
answer=0
def dfs(x,sum_v):
    global answer

    if sum_v==k:
        cnt=0
        for s in sl:
            check = True
            for c in s:
                if visited[ord(c)-ord('a')]==0:
                    check=False
                    break
            if check:
                cnt+=1
        answer=max(answer,cnt)
        return
    for i in range(x,26):
        if visited[i]==0:
            visited[i]=1
            dfs(i,sum_v+1)
            visited[i]=0

dfs(0,5)
print(answer)
