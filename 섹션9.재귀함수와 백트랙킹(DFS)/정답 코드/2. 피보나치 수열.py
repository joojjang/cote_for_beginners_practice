def DFS(n):
    if n == 1 or n == 2:
        return 1
    else:
        return DFS(n-2) + DFS(n-1)
              
print(DFS(5))

