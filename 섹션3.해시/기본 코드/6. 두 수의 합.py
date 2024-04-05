# 3 <= n <= 200,000 -> O(n) 이내로 풀 것 -> 반복문 한 번만
# 여기서 해시(딕셔너리)의 밸류는 별 의미 없음. 쓰는 이유는 그냥 시간복잡도가 작기 때문에

from collections import defaultdict

def solution(nums, target):
    answer = [0]*2
    checked = defaultdict(int)
    
    for i in range(len(nums)):
        x = nums[i]
        y = target - x # 짝꿍

        if y in checked:
            answer[0] = min(x, y)
            answer[1] = max(x, y)
            break
        else:
            checked[x] = 1
    
    return answer
                
print(solution([3, 7, 2, 12, 9, 15, 8], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))
'''
[3, 9]
[9, 15]
[12, 16]
[9, 17]
[-21, 7]
[0, 0]
'''
