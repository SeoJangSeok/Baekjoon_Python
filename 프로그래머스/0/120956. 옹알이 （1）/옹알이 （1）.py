def solution(babbling):
    answer = 0
    can_say = ['aya', 'ye', 'woo', 'ma']
    for word in babbling:
        for say in can_say:
            word = word.replace(say, ' ')
        if not word.strip():
            answer += 1
    return answer