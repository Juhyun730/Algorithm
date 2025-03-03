import sys
import bisect
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))

l.sort()
count=0

for i in range(len(l)):
    left=0
    right=len(l)-1
    while left<right:
        if l[left]+l[right]==l[i]:
            if left==i:
                left+=1
            elif right==i:
                right-=1
            else:
                count+=1
                break
        elif l[left]+l[right]>l[i]:
            right-=1
        else:
            left+=1

print(count)