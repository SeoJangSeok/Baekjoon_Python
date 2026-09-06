from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    target_dict = {w: n for w, n in zip(want, number)}
    
    # 연속 10일간의 할인 품목을 확인 (i는 회원가입 시작일)
    for i in range(len(discount) - 9):
        # i번째 날부터 10일간 할인하는 품목의 개수를 세기
        current_window = Counter(discount[i:i+10])
        
        # 원하는 품목과 수량이 완전히 일치하는지 확인
        if current_window == target_dict:
            answer += 1
            
    return answer