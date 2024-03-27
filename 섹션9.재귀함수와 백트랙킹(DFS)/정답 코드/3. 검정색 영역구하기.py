dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y, board):
    board[x][y] = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx >= 0 and nx < 5 and ny >= 0 and ny < 5 and board[nx][ny] == 1:
            DFS(nx, ny, board)
         
def solution(board):
    answer = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                answer += 1
                DFS(i, j, board)
    
    return answer
            
print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

