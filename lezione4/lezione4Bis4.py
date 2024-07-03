def majority_elements(nums: list[int]) -> int:
    """
    Data una lista di nums di n elementi, restituire l'elemento
    che compare piu di n/2 volte

    Esempio1: 
    nums : [3,2,3] -> restituire 3

    Esempio2:
    nums = [2,2,1,1,1,2] -> restituire None
    """
    
    d: dict[int, int] = {}
    for i in nums:
        d[i] = nums.count(i)
    
    lenght = len(nums)
    for key in d:
        d[key] /= lenght
        if d[key] > 0.5:
            return key
    return None
print(majority_elements([1,2,3,3,4,4,4,43,3,3,3,3,3,3,3,3,3]))