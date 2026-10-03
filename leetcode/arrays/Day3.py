# nums = [4, 7, 4, 2, 7, 7, 9]

# dicr = {}

# for num in nums:
#     if num in dicr:
#         dicr[num] += 1
#     else:
#         dicr[num] = 1

# print(dicr)


# def most_frequent(numbers):
#     dicr = {}
#     for num in numbers:
#         if num in dicr:
#             dicr[num] += 1
#         else:
#             dicr[num] = 1



#     highest_count = 0
#     most_common_number = 0

#     for key,value in dicr.items():
#         if value > highest_count:
#             highest_count = value
#             most_common_number = key

#     return most_common_number

# print(most_frequent([4, 7, 4, 2, 7, 7, 9]))
# print(most_frequent([5, 5, 2, 3, 5, 2]))
# print(most_frequent([8]))


def is_anagram(s, t):
    s_count_dict = {}

    for char in s:
        if char in s:
            s_count_dict += 1
        else:
            s_count_dict = 1
            
    t_count_dict = {}

    for char in t:
        if char in t:
            t_count_dict[char] += 1
        else:
            t_count_dict[char] = 1



is_anagram("anagram", "nagaram")
# True

is_anagram("rat", "car")
# False

is_anagram("aacc", "ccac")
# False
