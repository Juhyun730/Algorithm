import bisect

n=int(input())
l=list(map(int,input().split()))

l.sort() #1 5 7 9

# 바이섹트는 정렬된 리스트가 있을 때, 원소 x가 삽입될 위치를 반환함

#이분탐색
left=0
right=len(l)

'''while left<=right:
    mid=(left+right)//2
    cnt=0
    for i in range(n):
        cnt+=abs(l[i]-l[mid])
    '''
if len(l)%2==0:#짝수일때,
    mid1=(left+right)//2
    cnt1=0
    for i in range(n):
        cnt1+=abs(l[i]-l[mid1])

    mid2=(left+right)//2 - 1
    cnt2=0
    for i in range(n):
        cnt2+=abs(l[i]-l[mid2])

    if cnt1==cnt2 or cnt1 >cnt2:
        print(l[mid2])
    elif cnt1<cnt2:
        print(l[mid1])
else:
    mid1=(left+right)//2
    print(l[mid1])

