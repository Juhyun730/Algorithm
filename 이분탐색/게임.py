import math
x,y=map(int,input().split())

right=x
left=0
z=(100*y)//x
ans=x #최소 게임 실행 수


if z>=99:
    print(-1)
    exit(0)
else:
    while right>=left:
        mid=(right+left)//2 # 이긴 횟수중에 탐색할 값
        z1=(100*(y+mid))//(x+mid)

        if z1>z:
            ans=mid # 소수점이 바뀔때 그때그때 업데이트 한 값들을 ans로 저장
            right=mid-1

        else:
            left=mid+1

    print(ans)

