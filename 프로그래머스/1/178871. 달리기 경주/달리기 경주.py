def solution(players, callings):
    rank_map = {player: i for i, player in enumerate(players)}
    
    for player in callings:
        player_rank = rank_map[player] # 현재 불린 선수의 등수
        front_player = players[player_rank - 1] # 앞 선수
        players[player_rank - 1], players[player_rank] = players[player_rank], players[player_rank - 1]
        rank_map[player] -= 1
        rank_map[front_player] += 1
    return players