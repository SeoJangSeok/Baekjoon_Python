def solution(chicken):
    service_chicken = 0
    while chicken >= 10:
        service_chicken += chicken // 10
        chicken = chicken // 10 + chicken % 10
    return service_chicken