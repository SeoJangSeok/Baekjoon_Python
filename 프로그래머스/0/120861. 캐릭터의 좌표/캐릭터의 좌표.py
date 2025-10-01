def solution(keyinput, board):
    x_max, x_min = board[0] // 2, -(board[0] // 2)
    y_max, y_min = board[1] // 2, -(board[1] // 2)
    x, y = 0, 0
    
    for key in keyinput:
        if key == 'left' and x > x_min:
            x -= 1
        elif key == 'right' and x < x_max:
            x += 1
        elif key == 'up' and y < y_max:
            y += 1
        elif key == 'down' and y > y_min:
            y -= 1
    return [x, y]