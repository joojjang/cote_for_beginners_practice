def solution(nums):
    answer = -1
    once = []
    frequency = dict()

    for x in nums:
        if x in frequency:
            frequency[x] += 1
        else:
            frequency[x] = 1

    for key in frequency:
        if frequency[key] == 1:
            once.append(key)
    if len(once) != 0:
        answer = max(once)

    return answer
                            
                
print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))
'''
정답
8
-1
888
555
7
'''