def solution(nums):
    answer = 0
    count = 0

    for n in nums:
        if n == 1:
            count += 1 
        else: 
            if count > answer:
                answer = count
            count = 0

    # 맨 마지막 요소가 0이 아니라 1로 끝날 때도 answer 업데이트
    if count > answer:
        answer = count
    
    return answer

print(solution([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(solution([0, 0, 1, 0, 1, 0, 0]))
print(solution([1, 1, 1, 1, 1]))
print(solution([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))
# 5 1 5 3
