# def first_repeated(nums):
#     sets = set()

#     for num in nums:
#         if num in sets:
#             return num

#     sets.add(num)




# print(first_repeated([2, 5, 1, 2, 3, 5]))
# # 2

# print(first_repeated([1, 3, 4, 3, 2, 1]))
# # 3

# print(first_repeated([1, 2, 3, 4]))
# # None

# print(first_repeated([7, 7]))
# # 7


# def first_unique(nums):
#     counter = {}

#     for num in nums:
#         if num in counter :
#             counter[num] += 1
#         else:
#             counter[num] = 1


#     for num in counter:
#         # Change this counter to nums because iterating through counter affects time complexity
#         if counter [num] == 1:
#             return num



# print(first_unique([4, 5, 4, 6, 5, 7]))
# # 6

# print(first_unique([2, 2, 3, 3, 9]))
# # 9

# print(first_unique([1, 2, 1, 3, 2]))
# # 3

# print(first_unique([1, 1, 2, 2]))
# # None


# def common_elements(nums1, nums2):
#     res = set()

#     set1 = set(nums1)

#     for n in nums2:
#         if n in set1:
#             res.add(n)

#     lres = list(res)

#     return(lres)







# print(common_elements([1, 2, 2, 3, 4], [2, 2, 4, 6]))
# # [2, 4]

# print(common_elements([5, 1, 5, 7], [5, 5, 8]))
# # [5]

# print(common_elements([1, 2, 3], [4, 5, 6]))
# # []

# print(common_elements([], [1, 2]))
# # []



# def move_zeros(nums):
#     res = []
#     count  = []
#     for n in nums:
#         if n == 0:
#             count.append(n)
#         if n != 0:
#             res.append(n)
#     return res + count


# #o(n) both




# print(move_zeros([0, 1, 0, 3, 12]))
# # [1, 3, 12, 0, 0]

# print(move_zeros([0, 0, 1]))
# # [1, 0, 0]

# print(move_zeros([1, 2, 3]))
# # [1, 2, 3]

# print(move_zeros([0]))
# # [0]


def two_sum(nums, target):
    hashset = {}



    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashset:
            return [hashset[diff], i]
        else:
            hashset[n] = i







print(two_sum([2, 7, 11, 15], 9))
# [0, 1]

print(two_sum([3, 2, 4], 6))
# [1, 2]

print(two_sum([3, 3], 6))
# [0, 1]

print(two_sum([1, 2, 3], 10))
# None
