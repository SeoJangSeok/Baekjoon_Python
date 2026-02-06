def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    time = 0
    total_weight = 0
    
    while truck_weights:
        time += 1
        total_weight -= bridge.pop(0)
        
        if total_weight + truck_weights[0] <= weight:
            total_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
        
    time += bridge_length
    return time