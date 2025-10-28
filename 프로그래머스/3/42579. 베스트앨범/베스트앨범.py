def solution(genres, plays):
    genre_total = {}   # 장르별 총 재생 수
    genre_map = {}     # 장르별 [(재생 수, 인덱스)]

    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]

        # 총 재생 수 집계
        if g in genre_total:
            genre_total[g] += p
        else:
            genre_total[g] = p

        # 곡 목록 누적
        if g in genre_map:
            genre_map[g].append((p, i))
        else:
            genre_map[g] = [(p, i)]

    # 장르를 총 재생 수 내림차순으로 정렬
    ordered_genres = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)

    answer = []
    for g, _ in ordered_genres:
        songs = genre_map[g]
        # 재생 수 내림차순, 인덱스 오름차순
        songs_sorted = sorted(songs, key=lambda x: (-x[0], x[1]))
        # 상위 2곡 인덱스만 추가
        for _, idx in songs_sorted[:2]:
            answer.append(idx)

    return answer
