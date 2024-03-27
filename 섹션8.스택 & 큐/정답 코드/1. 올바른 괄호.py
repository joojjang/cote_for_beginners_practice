def solution(s):
    answer = "YES"
    stack = []
    for x in s:
        if x == ')':
            if len(stack) == 0:
                return "NO"
            stack.pop()
        else:
            stack.append(x)

    if len(stack) > 0:
        return "NO"

    return answer


print(solution("((()))()"))
print(solution("(()(()"))
print(solution("()())"))
print(solution("())("))
print(solution("((())))()("))
