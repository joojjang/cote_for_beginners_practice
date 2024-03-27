from collections import deque
def BFS(home):
    ch = [0] * 10001
    Q = deque()
    Q.append(0)
    ch[0] = 1
    L = 0
    while Q:
        n = len(Q)
        for i in range(n):
            x = Q.popleft()
            if x == home:
                return L
            for nx in [x-1, x+1, x+5]:
                if nx >= 0 and nx <= 10000 and ch[nx] == 0:
                    Q.append(nx)
                    ch[nx] = 1
        L += 1
                
 
def solution(home):
    answer = BFS(home)
    return answer
            
print(solution(10))
print(solution(14))
print(solution(25))
print(solution(24))
print(solution(345))
