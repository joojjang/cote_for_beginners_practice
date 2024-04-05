from collections import defaultdict

def solution(n, m, names):
    freq = defaultdict(int)
    nevernever = []

    for x in names:
        freq[x] += 1
    
    for key in freq:
        if freq[key] == 2:
            nevernever.append(key)

    # 출력
    # print("---")
    print(len(nevernever))
    for x in sorted(nevernever):
        print(x)

# 입력
arr = []
n, m = map(int, input().split())
for i in range(n+m):
    arr.append(input())

solution(n, m, arr)

'''
접근법
---
1. n줄만큼 돌면서 보도에 저장하고 
2. m줄만큼 돌면서 해당 이름이 보도에도 있다면
3. 정답 리스트에 저장하려고 했으나 
2번이 제대로 안 됨
-> 알고리즘 바꿈
1. 이름 key에 대응하는 value가 2라면 
2. 정답 리스트에 저장
'''