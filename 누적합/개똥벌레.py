import sys
input=sys.stdin.readline
import bisect
n,h=map(int,input().split())
a=[]
b=[]
for i in range(n):
    if i%2==0: #짝수인덱스일때 석순
        a.append(int(input()))
    else:
        b.append(h-int(input()))
ans=0
mymin=1e9
a.sort()
b.sort()

for nh in range(1,h+1): #가장 아래부터
    cnt=0
    aidx=bisect.bisect_left(a,nh)
    cnt+=len(a)-aidx
    bidx=bisect.bisect_left(b,nh)
    cnt+=bidx

    if mymin==cnt:
        ans+=1
    if mymin>cnt:
        mymin=cnt
        ans=1

print(mymin,ans)
# for nh in range(1,h+1): #가장 아래부터
#     ai=0 #석순인덱스
#     bi=0
#     cnt=0
#     for i in range(n):
#         if i%2==0: #짝수인덱스일때 석순
#             if nh <=a[ai]: #석순에 부딪힐때
#                 cnt+=1
#             ai+=1
#         else:
#             if nh >(h-b[bi]): #종유석에 부딪힐때
#                 cnt+=1
#             bi+=1
#     if cnt<mymin:
#         mymin=cnt
#         ans=1
#     elif cnt==mymin:
#         ans+=1
# print(mymin, ans)