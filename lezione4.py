def substract(a:float,b:float):
    x = a-b
    return x
a=23
b=12.45
print(substract(a, b))

"""
USIAMO UN FOR


def sum(l:list[float]) -> float :
    somma = 0
    for elem in l:
        somma += elem
    return somma

result = sum([1,2,3,4,5.66,546564,67.060606060,-123])
"""
"""
USIAMO UN WHILE

def sum(l:list[float]) -> float :
    somma = 0
    while i < len(l):
        somma += l[i]
        i += 1
    return somma

result = sum([1,2,3,4,5.66,546564,67.060606060,-123])

"""
i:int = int(input())
def check_value(i: int):
    if i > 5:
        print(f"{i} is bigger than 5")
    elif i < 5:
        print(f"{i} is smaller than 5")
    else:
        print(f"{i} is equal to 5")
check_value(i)


##############
x:str = str(input())

def check_lenght(x: str):
    if len(x) > 10:
        print(f"{x} is longer than 10 characters")
    elif len(x) < 10:
        print(f"{x} is shorter than 10 characters")
    else:
        print(f"{x} is equal to 10 characters")
check_lenght(x)


###############

def print_numbers(p:list):
    for v in p:
        print(v)
        
print_numbers([1,2,3,4,5,6,7,8,9])

##############
def check_each(w:list):
    for r in w:
        
        if r > 5:
            print(f"{r} is bigger than 5")
        elif r < 5:
         print(f"{r} is smaller than 5")
        else:
            print(f"{r} is equal to 5")
check_each([23,54,1,2,3,54,2,8,9])

