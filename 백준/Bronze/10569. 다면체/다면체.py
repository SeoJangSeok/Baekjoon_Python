for i in range(int(input())):
    peaks, lines = map(int, input().split())
    print(2 - (peaks - lines))