def rsp_winner(p1, p2, cards):
    # p1과 p2는 0-indexed 학생 번호
    c1, c2 = cards[p1], cards[p2]
    
    if c1 == c2:
        return p1
    elif (c1 == 1 and c2 == 3) or (c1 == 2 and c2 == 1) or (c1 == 3 and c2 == 2):
        return p1
    else:
        return p2

def tournament(i, j, cards):
    # 기저 조건: 1명만 남은 경우
    if i == j:
        return i
    
    # 두 그룹으로 분할
    mid = (i + j) // 2
    left = tournament(i, mid, cards)
    right = tournament(mid + 1, j, cards)
    
    # 두 그룹의 승자끼리 가위바위보
    return rsp_winner(left, right, cards)

# 테스트 케이스 처리
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    
    # 0번 인덱스부터 N-1번 인덱스까지 토너먼트 진행
    winner_idx = tournament(0, N - 1, cards)
    
    # 학생 번호는 1번부터 시작하므로 +1
    print(f"#{test_case} {winner_idx + 1}")