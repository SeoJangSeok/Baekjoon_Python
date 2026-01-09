import sys
input = sys.stdin.readline

n, m = map(int, input().split())
word_dict = {}

for _ in range(n):
    word = input().strip()
    
    # 길이 m 미만인 단어 무시
    if len(word) < m:
        continue
    
    # 단어 빈도수 갱신
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1
        
# 정렬 기준: 빈도수 내림차순, 길이 내림차순, 사전 순 오름차순
sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    
for word, _ in sorted_words:
    print(word)