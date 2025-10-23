def solution(phone_book):
    hash_map = {}
    for number in phone_book:
        hash_map[number] = 1

    for number in phone_book:
        head = ''
        for n in number:
            head += n
            if head in hash_map and head != number:
                return False
    return True