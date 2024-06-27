from context_manager import decorator
from merge import mergeSort


@decorator
def area_cerchio(raggio : float):
    return raggio * raggio * 3.14

mergeSort = decorator(mergeSort)


class Analisi:
    def tempo(func):
        def wrapper(*args):
            import time

            start = time.time()

            func(*args)

            print(f"time elapsed :{ time.time() - start}")

        return wrapper
    
@Analisi.tempo
def area_cerchio(raggio : float):
    return raggio * raggio * 3.14

area_cerchio(1)