import sys
input = sys.stdin.readline
n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()

end=l[-1]
start=0

def tree(ll,h):
    result=0
    for i in ll:
        now = i-h
        if now>0:
            result+=now
    return result #가져가는 나무 합

ans =0
while start<=end :
    mid = (start+end)//2
    cnt = tree(l,mid)
    if cnt<m:
        end = mid-1
        
    elif cnt>=m :
        start = mid+1
        ans = mid
print(ans)