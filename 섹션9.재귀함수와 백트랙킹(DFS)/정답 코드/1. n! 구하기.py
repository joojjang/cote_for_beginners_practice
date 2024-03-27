def DFS(n):
    if n == 1:
        return 1
    else:
        return n * DFS(n-1)

print(DFS(5))             
print(DFS(6))
