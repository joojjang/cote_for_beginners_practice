# nums[i]의 최댓값 1,000이므로 direct address table 이용해도 무리 없음

def solution(nums):
    answer = -1
    cnt = [0] * 1001
    for x in nums:
        cnt[x] += 1

    '''
    direct address table의 특성을 이용하면 (배열 인덱스 순서 = 오름차순)
    최댓값이 정답이 되어야 하니까
    for i in range(1, 1001) 할 필요 없이
    내림차순으로 돌면 됨
    '''
    for i in range(1000, 0, -1):
        if cnt[i] == 1:
            return i
       
    return answer
                            
                
print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))
