
# def majority_element(nums):
#     seen = {}
#     for n in nums:
#         if n in seen:
#             seen[n] += 1
#         else:
#             seen[n] =1

#         if seen[n] > len(nums) / 2:
#                     return n


# nums = [3, 3, 4, 3, 2, 3, 3]


nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6, 8]

# [1, 2, 3, 4, 5, 6, 7, 8]
def merge_sorted(nums1, nums2):
    left = 0
    right = 0
    res = []

    while(left < len(nums1) and right < len(nums2) ):
        if nums1[left] < nums2[right]:
            res.append(nums1[left])
            left += 1
        else:
            res.append(nums2[right])
            right += 1

        if len(nums1) == left:
            res.append(nums2)
        else:
            res.append(nums1)
    return res

merge_sorted(nums1,nums2)
