import sys
input=sys.stdin.readline

n,c=map(int,input().split())
l=[]
for _ in range(n):
    l.append(int(input()))
l.sort()
# 공유기의 개수는 c
# 공유기를 가능한 거리를 최대로 설치한다음, 공유기들 사이의 거리에서 가장 인접한 두 공유기 사이의 거리 출력하기
# 방법: 공유기 사이의 거리를 이분탐색하기
start=1 #최소거리
end=l[-1]-l[0]

while start <=end:
    mid=(start+end)//2 #현재 공유기의 거리
    current = l[0] # 일단 하나 설치하자
    count=1 
    #중간 거리로 공유기 설치
    for i in range(1,n):
        if l[i] >= current+mid: #이전에 설치된 집과의 거리가 mid 이상인 경우
            current=l[i] #공유기 설치
            count+=1
    if count >=c:
        start = mid +1 #거리를 더 늘려도 됨
        result=mid
    else: #c개 이상의 공유기를 설치할 수 없는 경우, 거리 감소
        end=mid-1
print(result)