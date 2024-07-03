def move_zeroes(nums: list[int]):
    """
    Data una lista nums di interi, spostare gli zeri alla fine di questa lista
    mantenendo l'ordine originale dei numeri che non sono zeri

    Esempio1:
    nums = [0,1,0,3,12] -> modifica la lista in [1,3,12,0,0]

    """
    
    for i in range(len(nums)):
        if nums[i] == 0:
            #x = nums.pop(i)
            nums.append(nums.pop(i))
    return nums
print(move_zeroes([0,2,3,0,0,2,3]))

    