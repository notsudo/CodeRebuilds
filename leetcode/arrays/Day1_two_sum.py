nums = [2, 7, 11, 15]
target = 9

def two_sum (nums, target):
    for i, n in enumerate(nums):
        difference = target - n
        for j in range (i + 1, len(nums)):
            if nums[j] == difference:
                return [i, j]
# THis is the brute force solution which is 0(n)^2
