def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    new_list:list = []
    for element in nums1:
        if element in nums2:
            new_list.append(element)
    return set(new_list)
print(intersection([1,2,3,4,5,6,7,8,9], [1,9,80,56,3,2]))
