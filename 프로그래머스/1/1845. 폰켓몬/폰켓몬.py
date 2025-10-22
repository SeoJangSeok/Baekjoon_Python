def solution(nums):
    nums_len = len(nums)
    return nums_len // 2 if len(set(nums)) >= nums_len // 2 else len(set(nums))