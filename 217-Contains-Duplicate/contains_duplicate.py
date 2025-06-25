def contains_duplicate(nums):
    # Approach 1
    # Use set to keep track of numbers seen if a number already exists in the tracker, its dupes

    tracker = set()
    for num in nums:
        if num in tracker:
            return True
        tracker.add(num)
    return False


# Space Complexity : O(n)
# Time Complexity :O(n)


def contains_duplicate2(nums):
    #  Approach 2
    # Sort the array first
    #  Check adjacent elements
    #  Uses less space than Approach 1 but much slower

    nums.sort()

    if len(nums) <= 1:
        return False

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


#  Space Complexity : O(1) if in place sorting
# Time Comlexity: O(n log n) due to sorting
#  Main trade-off - Approach1 is faster(O(n)) but uses more space(O(n)), Approach 2 is slower(O(n log n)) but uses less space (O(1))
#  Both are valid approaches and have their use cases


# Alt Code for Approach 2
#  nums.sort()

#         if len(nums) <= 1:
#             return False

#         i = 0
#         j =  i + 1

#         while j < len(nums):
#             if nums[i] == nums[j]:
#                 return True
#             i+=1
#             j+=1
#         return False
