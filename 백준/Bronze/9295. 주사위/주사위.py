test_case = int(input())

for index, _ in enumerate(range(test_case)):
    dice_1, dice_2 = map(int, input().split())
    print(f'Case {index + 1}: {dice_1 + dice_2}')