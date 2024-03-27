from bisect import bisect_left, bisect_right
def solution(nums, weight):
    answer = bisect_right(nums, weight)
    return -1 if answer == len(nums) else answer
    
    
print(solution([70, 80, 80, 80, 80, 90, 90, 90], 79)) 
