nums = [2, 7, 11, 15]
target = 9

def two_sum (nums, target):
    for i, n in enumerate(nums):
        difference = target - n
        for j in range (i + 1, len(nums)):
            if nums[j] == difference:
                return [i, j]
# THis is the brute force solution which is 0(n)^2 Time and 0(1)Space


def two_sum_optimized(nums, target):
    seen = {}

    for i, n in enumerate(nums):
        difference = target - n

        if difference in seen:
            return [seen[difference], i]
        else:
            seen[n] = i

print(two_sum_optimized([2, 7, 11, 15], 9))
# this one has 0(n) Space 0(n)
