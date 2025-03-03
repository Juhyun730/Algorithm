n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열
interval_sum=0
end=0
count=0

for s in range(len(data)):
    while interval_sum < m and end<n:
        interval_sum+=data[end]
        end+=1
    if interval_sum==m:
        count+=1
    interval_sum-=data[s]
print(count)