n, m = map(int, input().split())
pokemon_name = {}
pokemon_num = {}

for i in range(n):
    name = input()
    pokemon_name[name] = i + 1
    pokemon_num[i + 1] = name

for _ in range(m):
    search = input()
    if search.isdigit():
        print(pokemon_num[int(search)])
    else:
        print(pokemon_name[search])