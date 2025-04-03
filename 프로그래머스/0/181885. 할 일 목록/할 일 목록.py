def solution(todo_list, finished):
    not_finished = []
    for i, boolean in enumerate(finished):
        if boolean == False:
            not_finished.append(todo_list[i])
    return not_finished