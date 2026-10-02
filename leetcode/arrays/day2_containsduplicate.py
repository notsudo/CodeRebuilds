# def contains_duplicate(nums):
#     for i,n in enumerate(nums):
#         for j in range(i+1, len(nums)):
#             if nums[j] == n:
#                 return True
#     return False

# Time:  O(n²)
# Space: O(1)


def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        else:
            seen.add(n)
    return False

# Time:  O(n) average
# Space: O(n)

print(contains_duplicate([1, 2, 3, 1]))
# True

print(contains_duplicate([1, 2, 3, 4]))
# False

print(contains_duplicate([5, 5]))
# True

print(contains_duplicate([1]))
# False
