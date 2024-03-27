def solution(nums):
    answer = []
    n = len(nums)
    minN = 1000000000
    for i in range(n):
        for j in range(i+1, n):
            diff = abs(nums[i] - nums[j])
            if diff < minN:
                minN = diff

    for i in range(n):
        for j in range(i+1, n):
            diff = abs(nums[i] - nums[j])
            if diff == minN:
                answer.append(sorted([nums[i], nums[j]]))
                
    return answer

print(solution([3, 8, 1, 5, 12]))
print(solution([2, 1, 3, 5, 4]))
print(solution([5, 10, 15, 20, 25, 11]))
print(solution([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
print(solution([100, 200, 300, 400, 120, 130, 135, 132, 121]))
