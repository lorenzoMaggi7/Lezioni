###black jack
def blackjack(hand: list[int]) -> int:
    total_sum: int = sum(hand)
    num_aces: int = hand.count(1) + hand.count(11)
    while total_sum > 21 and num_aces != 0:
        total_sum -= 10
        num_aces -= 1

    return total_sum

print(blackjack([2,3,5])) #10
print(blackjack([11,5,5])) #21
print(blackjack([1,10,11])) #12
print(blackjack([1,10,5])) # 16
print(" ")
####rettangoli
"""
Uno sviluppatore web deve sapere come progettare le dimensioni di una pagina web. Pertanto, data l'area specifica di una pagina Web rettangolare, 
il tuo compito ora è progettare una pagina Web rettangolare, la cui lunghezza L e larghezza W soddisfino i seguenti requisiti:

1. L'area della pagina web rettangolare che hai progettato deve essere uguale all'area di destinazione specificata.
2. La larghezza W non deve essere maggiore della lunghezza L, il che significa L >= W.
3. La differenza tra la lunghezza L e la larghezza W dovrebbe essere la minima possibile.

Restituisce una lista [L, W] dove L e W sono la lunghezza e la larghezza della pagina web che hai progettato in sequenza.

Esempio:

construct_rectangle(4)

L'area target è 4 e tutti i modi possibili per costruirla sono [1,4], [2,2], [4,1].
Ma secondo il requisito 2, [1,4] è illegale; secondo il requisito 3, [4,1] non è ottimale rispetto a [2,2]. Quindi la lunghezza L è 2 e la larghezza W è 2.
"""
def divisors(n):
    result = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            result.append(i)
    result.append(n)
    return result

def construct_rectangle(area:float) -> list[float]:
    
    min_dist = area - 1
    props = []
    dividers = divisors(area)
    for i in dividers:
        for j in dividers:
            if area == (i*j):
                dist = abs(i - j)
                if dist <= min_dist:
                    min_dist = dist
                    props = [i,j]

    return props

print(construct_rectangle(37))
print(construct_rectangle(122122))
print(construct_rectangle(49))
print(" ")

"""def construct_rectangle(area:int) -> list[float]:
    result: list[int] = []
    half_area: int = int(area **0.5)
    for i in range(1,area+1):
        for j in range(i, half_area+1):
            if  i >= j and i * j == area:
                result.append([i,j])


    diff_min:float = float('inf')
    index: int= 0
    for i in range(len(result)):
        curr_diff: float = abs(result[i][0] - result[i][1])
        if curr_diff <= diff_min:
            diff_min = curr_diff
            index = i

    return result[index]"""

"""def construct_rectangle(area:int) -> list[int]:
    sqrt_area = int(area **0.5)
    for width in range(sqrt_area, 0, -1):
        if area % width ==0:
            height = area // width
            return[height,width]"""


"""
date due stringhe note e magazine, restituisci true se note può essere costruita utilizzando le lettere di magazine e false in caso contrario.
ogni lettera nelle magazine può essere utilizzata solo una volta in note
"""
def ransom(note: str, magazine: str) -> bool:
    char_count: dict[str,int] = {}
    for char in magazine:
        #metodo alternativo per scrivere l'if presente qui sotto
        char_count[char] = char_count.get(char,0) + 1
        """if char in char_count:
            char_count[char] = char_count[char] +1
        else:
            char_count[char] = 0"""

    for char in note:
        if char_count.get(char,0) == 0:
            return False
        char_count[char] -= 1

    return True
    

print(ransom("a", "b"))
print(ransom("aa","aab"))


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#########################################################################################################################################################
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def binary_search(array:list[int], x : int) -> int:
    return __binary_search(array, x, 0, len(array))


def __binary_search(array: list[int], x: int, low: int, high: int) -> int:
    if low > high:
        return None
    
    mid =(low + high) // 2
    if x == array[mid]:
        return mid
    else:
        if x > array[mid]:
            return __binary_search(array, x, mid + 1, high)
        else:
            return __binary_search(array, x, low, mid -1)



def binary_search_iterative(array: list[int], x: int) -> int:
    low, high = 0, len(array)
    while low < high:
        mid = (low + high) // 2
        if x == array[mid]:
            return mid
        elif x > array[mid]:
            low = mid + 1
        else:
            high = mid - 1

array: list[int] = [1,2,3,4,5, 29109, 202011]
array.index(5)


def visit_tree(d: dict[int, list[int]], n:int):
    print(n)
    left_child, right_child = tree[n]
    if left_child != None:
        visit_tree(tree,left_child)
    if right_child != None:
        visit_tree(tree, right_child)


tree = {1:[2,3],2:[4,5],3:[None,None],4:[None,None],5:[None,None]}
visit_tree(tree, 1)
print(" ")

def visiting_tree_iterative(tree: dict[int, list[int]],root: int):
    stack: list[int] = [root]
    while stack: #while len(stack) != 0
        curr_node = stack.pop()
        if curr_node != None:
            print(curr_node)
            left_child, right_child = tree[curr_node]
            if right_child: #if right_child != 0
                stack.append(right_child)
            if left_child:  #if left_child != 0
                stack.append(left_child)

visiting_tree_iterative(tree,1)

#####calcola la media per ciascun livello
