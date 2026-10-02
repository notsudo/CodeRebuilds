# 1. Given:
nums = [4, 7, 2, 7, 9, 4, 7]

# Count how many times 7 appears.
# Do NOT use .count()
counter = 0

for num in nums:
    if num == 7:
        counter += 1
print(counter)


# 2. Find the smallest number without using min().
# Must work with negative numbers too.
sm_num = nums[0]
for num in nums:
    if num < sm_num:
        sm_num = num
print(sm_num)



# 3. Create a function:
# count_even(numbers)
#
# Return how many even numbers are in the list.
def count_even(numbers):
    counter = 0
    for num in numbers:
        if num % 2 == 0:
            counter += 1
    return counter



# 4. Create a function:
# contains_number(numbers, target)
#
# Return True if target exists in numbers.
# Otherwise return False.

def contains_number(numbers, target):
    for num in numbers:
        if target == num:
            return True

    return False
