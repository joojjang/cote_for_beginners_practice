from collections import deque
def BFS():
    Q = deque()
    Q.append(1)
    L = 0
    while Q:
        n = len(Q)
        print(L, end = " : ")
        for i in range(n):
            v = Q.popleft()
            print(v, end = " ")
            for nv in [v*2, v*2+1]:
                if nv > 7:
                    continue
                Q.append(nv)
        print()
        L += 1
                          
BFS()
