s = input()
s_set = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        s_set.add(s[i:j+1])
print(len(s_set))