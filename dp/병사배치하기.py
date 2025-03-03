'''import sys
import bisect
import copy
input=sys.stdin.readline

count=0
n=int(input())
l=list(map(int,input().split()))

l.reverse()
cnt=[]

for i in l:
    pos = bisect.bisect_left(l,i)

    if pos==len(cnt):
        cnt.append(i)
    else:
        cnt[pos]=i
print(n-len(l))'''
    



# 15, 11, 3, 4, 8
# 3,4,[],11,15 <=이분탐색이면 []에 8이 들어감    
'''import sys
import bisect
import copy
input=sys.stdin.readline

count=0
n=int(input())
l=list(map(int,input().split()))

dp=[1]*n

for i in range(1,n):
    for j in range(i):
        if l[i] <l[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp))'''

import bisect

n = int(input())
l = list(map(int, input().split()))

# 리스트 l의 값을 뒤집어 줌 (내림차순 문제를 오름차순으로 변환)
l.reverse()

# LIS 배열을 담을 리스트
lis = []

for soldier in l:
    # 현재 병사가 들어갈 위치를 이분 탐색으로 찾기
    pos = bisect.bisect_left(lis, soldier)
    
    # 만약 병사가 LIS 배열의 끝에 들어갈 수 있다면 추가
    if pos == len(lis):
        lis.append(soldier)
    else:
        # 아니라면 그 위치의 값을 갱신
        lis[pos] = soldier

# 제외해야 할 병사의 수 = 전체 병사의 수 - LIS의 길이
print(n - len(lis))