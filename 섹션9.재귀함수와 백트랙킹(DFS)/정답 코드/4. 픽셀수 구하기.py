dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
def DFS(x, y, board):
    global cnt
    board[x][y] = 0
    cnt += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx >= 0 and nx < 5 and ny >= 0 and ny < 5 and board[nx][ny] == 1:
            DFS(nx, ny, board)
    

def solution(board):
    global cnt
    answer = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                cnt = 0
                DFS(i, j, board)
                answer.append(cnt)
    
    return answer
            
print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

