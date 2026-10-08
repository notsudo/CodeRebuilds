
def majority_element(nums):
    seen = {}
    for n in nums:
        if n in seen:
            seen[n] += 1
        else:
            seen[n] =1

        if seen[n] > len(nums) / 2:
                    return n


nums = [3, 3, 4, 3, 2, 3, 3]
