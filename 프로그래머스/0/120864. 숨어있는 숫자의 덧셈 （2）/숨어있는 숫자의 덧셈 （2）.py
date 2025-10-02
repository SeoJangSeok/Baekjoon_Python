def solution(my_string):
    for char in my_string:
        if char.isalpha():
            my_string = my_string.replace(char, ' ')
    return sum(map(int, my_string.split()))