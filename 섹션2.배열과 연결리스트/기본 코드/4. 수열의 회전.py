from collections import deque

def solution(nums, k):
    answer = deque(nums) # 시간복잡도 줄이기 위함
    count = 0
    
    for n in nums:
        if count < k:
            answer.popleft()
            answer.append(n)
            count += 1

    return list(answer)

print(solution([3, 7, 1, 5, 9, 2, 8], 3))
print(solution([2, 12, 2, 1, 3, 3, 9], 2))
print(solution([1, 2, 5, 4, 6, 7, 9], 6))
print(solution([1, 3, 6, 8, 14, 2, 1, 7], 5))
# 정답
# [5, 9, 2, 8, 3, 7, 1]
# [2, 1, 3, 3, 9, 2, 12]
# [9, 1, 2, 5, 4, 6, 7]
# [2, 1, 7, 1, 3, 6, 8, 14]
