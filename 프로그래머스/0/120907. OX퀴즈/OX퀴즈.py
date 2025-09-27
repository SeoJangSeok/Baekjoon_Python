def solution(quiz):
    answer = []
    for q in quiz:
        q = q.split(' = ')
        x, op, y = q[0].split()
        
        if op == '+':
            result = int(x) + int(y)
        else:
            result = int(x) - int(y)
        answer.append('O' if result == int(q[1]) else 'X')

    return answer