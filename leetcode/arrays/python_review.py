#Problem 1
#problem was write an arr and print out every number greater than 4

arr = [3,7,2,9,4]

# forgot that range only takes a integer so u cant put in the list
#len() => gives back the length of the arr

# for i in range(len(arr)):
#     if arr[i] > 4:
#         print (arr[i])

#in python you can directly access the number in the array and not require the index to retrieve that number
# for number in arr:
#     if number > 4:
#         print( arr[i])

#Problem 2
#Add all the numbers in the arr to a sum without using the sum() function

# total = 0
# for num in arr:
#     total = num + total
#     #shortcut is this total += num
# print(total)

#Problem 3
track = arr[0]
#dont use 0 because what if the array stored negative numbers
# for num in arr:
#     if num > track:
#         track = num
# print(track)


# 1. Given [3, 7, 2, 9, 4], print every number > 4.
list1 = [3,7,2,9,4]
# for num in list1:
#     if num > 4:
#         print(num)
# 2. Calculate the sum without sum().
# sum = 0
# for num in list1:
#     sum += num

# print(sum)

# 3. Find the largest number without max().
#    Must also work with negative numbers.
large_num = list1[0]
for num in range(len(list1)):
    if large_num > num:
        large_num = num

# 4. Count how many numbers are even.
even_counter = 0

# 5. Create a function:
#       double(number)
#    that RETURNS twice the number.

# 6. Create:
#       is_even(number)
#    that returns True or False.

# 7. Create:
#       find_largest(numbers)
#    that returns the largest number.

# 8. Create a dictionary containing:
#       username → "notsudo"
#       language → "Python"
#       problems → 0

#    Print the language.

# 9. Change problems from 0 → 1.

# 10. Loop through the dictionary and print
#     every key and value.
