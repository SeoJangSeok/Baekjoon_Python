while True:
    try:
        n = int(input())
    except:
        break
    x = 1 # 각 자릿수가 1로만 이루어진 수
    count = 1 # 자릿수
    while True:
        if x % n == 0: # x가 n의 배수인 경우
            break
        else: # 아니라면
            x = x * 10 + 1 # 자릿수 증가
            count += 1
    print(count)