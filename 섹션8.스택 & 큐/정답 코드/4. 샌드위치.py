def solution(nums):
    answer = 0
    stack = []
    for x in nums:
        if x == 1 and len(stack) >= 2 and stack[-1] == 2 and stack[-2] == 1:
            answer += 1
            stack.pop()
            stack.pop()
        else:
            stack.append(x)
    
    return answer
    

print(solution([1, 1, 1, 2, 1, 1, 2, 1, 2, 1]))
print(solution([2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1]))
print(solution([1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1]))
print(solution([2, 1, 1, 1, 2, 1, 2]))
print(solution([1, 1, 1, 1, 1, 1, 1]))
