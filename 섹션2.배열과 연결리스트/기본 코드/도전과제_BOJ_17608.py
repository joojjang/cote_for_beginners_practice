# 시간 초과
def solution(sticks):
    answer = 1 # 보이는 막대기 개수
    n = len(sticks)
    longest = sticks[-1]

    for i in range(n - 1, -1, -1):
        if sticks[i] > longest:
            answer += 1
            longest = sticks[i]
   
    return answer


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print(solution(arr))

'''
맨마지막 막대기는 보임. 그래서 기본값이 1
마지막에서 두 번째 막대기부터 첫 번째 막대기까지 for문 돌면서
맨마지막 막대기보다 긴 길이 나올 때마다 answer += 1
'''
