def generatore():

    yield "A"
    yield "B"
    yield "C"


prova_generatore = generatore()

print(next(prova_generatore))
print(next(prova_generatore))
print(next(prova_generatore))

import time
from contextlib import contextmanager

@contextmanager
def context_manager_decorator(*args):
    import time

    start_time : float = time.time()
    
    yield

    end_time : float = time.time()
    elapsed_time : float = end_time - start_time
    print(f"{elapsed_time}")

@context_manager_decorator
def area_cerchio(raggio : float):

    return raggio * raggio * 3.14

area_cerchio(1)


import sys 

a = []
b = a
print(sys.getrefcount(a))

threads : list = []

def thread_function(name):

    print(f"{name} Time - {time.time()}")
    time.sleep(2)
    print(f"{name} Time - {time.time()}")

import threading
for i in range(3):

    x = threading.Thread(target=thread_function, args= (1, ))
    threads.append(x)
    x.start()


for i in threads:
    i.join()
    




print(f"Prima di thread")
x.start()
print(f"Thread partito")
x.join()
print(f"Thread finito????")
