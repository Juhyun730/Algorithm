import sys
from itertools import combinations

input=sys.stdin.readline


n=int(input())
l=[]
while 1:
    for i in range(1,11):
        curl=list(combinations([x for x in range(10)],i))
        
        for c in curl:
            l.append(int(''.join(sorted(list(map(str,c)))[::-1])))

        if len(l)<=n:
            continue
        else:
            l.sort()
            print(l[n])
            exit(0)

    print(-1)
    exit(0)