from collections import deque

def solution(nums):
    answer = deque()

    for n in nums:
        if n in answer:
            continue
        else: 
            answer.appendleft(n)

    answer = list(answer)

    # list로 풀기
    # answer = []

    # for n in nums:
    #     if n in answer:
    #         continue
    #     else:
    #         answer.append(n)

    # answer.sort(reverse=True)

    return answer
    
print(solution([0, 1, 1, 1, 2, 2, 2, 3]))
print(solution([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5]))
print(solution([0, 0, 0, 3, 3, 3, 5, 7, 7, 7]))
print(solution([1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]))
# [3, 2, 1, 0]
# [5, 4, 3, 2, 1]
# [7, 5, 3, 0]
# [9, 8, 7, 6, 5, 4, 3, 2, 1]
