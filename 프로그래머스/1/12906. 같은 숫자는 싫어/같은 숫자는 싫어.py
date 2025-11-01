def solution(arr):
    stack = []
    for i in range(len(arr)):
        # stack이 비어있을 경우
        if not stack:
            stack.append(arr[i])
        # stack에 값이 있는 경우
        else:
            if stack[-1] != arr[i]:
                stack.append(arr[i])
            else:
                continue
    return stack