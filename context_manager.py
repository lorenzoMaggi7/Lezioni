# #####################################################################
# import time

# class Timer:
#     def __enter__(self):
#         self.start_time = time.time()
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.end_time = time.time()
#         self.elapsed_time = self.end_time - self.start_time
#         print(f"Time elapsed: {self.elapsed_time} seconds")
#         # Gestione delle eccezioni: restituendo False, le eccezioni saranno propagate
#         return False

# # Utilizzo del context manager Timer
# with Timer():
#     time.sleep(1)

import random
import time

from merge import mergeSort


class FIleManager:

    def __init__(self, filename : str,mode : str ):
        self.filename = filename
        self.mode = mode
        
    def __enter__(self):
        self.filewrapper = open(self.filename, self.mode)

        return self.filewrapper

    def __exit__(self, exc_type, exc_value, traceback):
        
        self.filewrapper.close()

with FIleManager(filename="prova.txt", mode="w") as file:

    file.write("Ciao")

with open("prova.txt", "w") as file:

    file.write("Ciao")


class Timer:

    def __enter__(self):
        self.time = time.time()

    def __exit__(self,exc_type, exc_value, traceback):
        print(f"Time Elapsed: {time.time() - self.time}")


with Timer():

    time.sleep(1)

lista = [random.randint(0,10000) for _ in range(10)]

with Timer():

    mergeSort(lista)



# def ciao(name:str):

#     return f"Ciao, {name}"

# def salve(name):
#     return f"Salve, {name}"

# def saluta(func) -> str:

#     return func("Bob")

def parent():
    print("Sono in parent")

    def first_child():
        print("Sono in first child")

    def second_child():
        print("Sono in second child")


    second_child()
    second_child()
    first_child()

parent()

def decorator(func):
    def wrapper():
        print(f"Prima di func")

        func()

        print(f"Dopo di func")


    return wrapper

def ciao():
    
    print("ciao")



def decorator(func):
    def wrapper(*args):
        start = time.time()

        func(*args)
        print(func)
        print(f"Time Elapsed: {time.time() - start}")

    return wrapper




mergeSort = decorator(mergeSort)
lista = [random.randint(0,10000) for _ in range(100000)]
mergeSort(lista)



# ciao = decorator(ciao)

# ciao()


# print(saluta(ciao)) 
# print(saluta(salve))