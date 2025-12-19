def isprime(num):
    if num == 0 or num == 1:   #0과 1을 처리
        return False
    elif num == 2:
        return True

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    else:
        return True

num=int(input())
for _ in range(num):
    test= int(input())
    while True: 
        if isprime(test):      
            print(test)
            break
        else:
            test+=1