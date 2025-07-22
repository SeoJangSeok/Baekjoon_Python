remained_apple = 0
for school in range(int(input())):
    students, apples = map(int, input().split())
    remained_apple += apples % students
print(remained_apple)