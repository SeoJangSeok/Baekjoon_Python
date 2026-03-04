import sys

input = sys.stdin.readline


def divide_and_conquer(heights, start, end):
    if start == end:
        return heights[start]

    mid = (start + end) // 2
    left_area = divide_and_conquer(heights, start, mid)
    right_area = divide_and_conquer(heights, mid + 1, end)

    left = mid
    right = mid
    min_height = heights[mid]
    mid_area = min_height

    while start < left or right < end:
        if right < end and (left == start or heights[left - 1] < heights[right + 1]):
            right += 1
            min_height = min(min_height, heights[right])
        else:
            left -= 1
            min_height = min(min_height, heights[left])

        mid_area = max(mid_area, min_height * (right - left + 1))

    return max(left_area, right_area, mid_area)


results = []

while True:
    row = list(map(int, input().split()))
    if row[0] == 0:
        break

    heights = row[1:]
    results.append(divide_and_conquer(heights, 0, len(heights) - 1))

sys.stdout.write("\n".join(map(str, results)))
