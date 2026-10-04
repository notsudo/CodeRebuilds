# def count_vowels(text):
#     vowels = ["a","e","i","o","u"]
#     counter = 0

#     for l in text:
#         if l in hold:
#             counter +=1
#     return counter



# print(count_vowels("hello"))
# # 2

# print(count_vowels("computer science"))
# # 6

# print(count_vowels("xyz"))
# # 0


# def reverse_string(text):
#     res = ""

#     for i in range(len(text) - 1, -1,-1):

#         res += text[i]
#     return res


# print(reverse_string("hello"))
# # "olleh"

# reverse_string("oscar")
# # "racso"

# reverse_string("a")
# # "a"


# def is_palindrome(text):
#     res = ""

#     for i in range(len(text) - 1, -1, -1):
#         res += text[i]
#     return res == text

# print(is_palindrome("racecar"))
# # True

# print(is_palindrome("level"))
# # True

# print(is_palindrome("hello"))
# # False

# print(is_palindrome("a"))
# # True

#This has a time and space complexity of o(n)

# def is_palindrome_two_pointer(text):
#     left = 0
#     right = len(text)-1

#     while left < right:
#         if text[left] == text[right]:
#             left += 1
#             right -= 1
#         else:
#             return False
#     return True

# Has a time complexity of o(n) but a space complexity of o(1)

nums = [1, 2, 4, 6, 8, 9]
target = 10

def has_pair_sum(nums, target):
    left = 0
    right = len(nums) -1

    while (left < right) :
        if nums[left] + nums[right] != target :
            left += 1
        if nums[left] + nums[right] == target :
                    return True
    return False


has_pair_sum([1, 2, 4, 6, 8, 9], 10)
# True   because 1 + 9 = 10

has_pair_sum([1, 2, 4, 6, 8, 9], 20)
# False

has_pair_sum([1, 3, 5, 7], 8)
# True




def has_pair_sum(nums, target):
    left = 0
    right = len(nums) -1

    while (left < right) :
        # current_sum = nums[left] + nums[right] use this so u dont do the addition 3 times
        if nums[left] + nums[right] == target:
            return True
        elif nums[left] + nums[right] < target :
                    left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
    return False

# Time: O(n)
# Extra space: O(1)




nums = [1, 1, 2, 2, 3, 4, 4]

def remove_duplicates(nums):
    dups = []

    for n in  nums:
        if n not in dups:
            dups.append(n)
    return dups

# Time: O(n²)
# Space: O(n)

def remove_duplicates(nums):
    seta = set(nums)
    lnums = list(seta)

    return lnums

# Time: O(n)
# Space: O(n)

def remove_duplicates(nums):
    if len(nums)  == 0:
        return []
    # this line would crash if array was empty
    dup = [nums[0]]
    left = 0
    right = 1
    #want right to stay in bounds of array
    while (right < len(nums) ):
        if nums[right] != nums[left] :
            dup.append(nums[right])
        left += 1
        right += 1
    return dup

# Time: O(n) because we make one pass through the list.
# Extra space: O(n) because dup can grow to contain every number if they're all unique.
