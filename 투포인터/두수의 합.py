import sys

input=sys.stdin.readline

n=int(input())
l=list(map(int,input().split()))
l.sort()

x=int(input())
count=0
mysum=0
end=n-1
start=0

while start<end:
    mysum=l[start]+l[end]
    if mysum==x:
        count+=1
    if mysum<x:
        start+=1
        continue
    end-=1


print(count)


