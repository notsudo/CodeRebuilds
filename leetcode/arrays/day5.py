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


def first_unique(nums):
    counter = {}

    for num in nums:
        if num in counter :
            counter[num] += 1
        else:
            counter[num] = 1


    for num in counter:
        # Change this counter to nums because iterating through counter affects time complexity
        if counter [num] == 1:
            return num



print(first_unique([4, 5, 4, 6, 5, 7]))
# 6

print(first_unique([2, 2, 3, 3, 9]))
# 9

print(first_unique([1, 2, 1, 3, 2]))
# 3

print(first_unique([1, 1, 2, 2]))
# None


