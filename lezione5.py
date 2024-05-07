
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
    result: dict= {}
    while stack: #while len(stack) != 0
        curr_node = stack.pop()
        if curr_node != None:
            left_child, right_child = tree[curr_node]
            if right_child: #if right_child != 0
                stack.append(right_child)
            if left_child:  #if left_child != 0
                stack.append(left_child)
                
visiting_tree_iterative(tree,1)

#####calcola la media per ciascun livello
def visiting_tree_iterative(tree: dict[int, list[int]],root: int):
    stack: list[int] = [(root, 0 )]
    node_numb = {}
    result: dict= {}
    while stack: #while len(stack) != 0
        curr_node, curr_level = stack.pop()
        result[curr_level] = result.get(curr_level, 0) + curr_node
        node_numb[curr_level] = node_numb.get(curr_level, 0) +1
        if curr_node != None:
            left_child, right_child = tree[curr_node]
            if right_child: #if right_child != 0
                stack.append(right_child, curr_level + 1)
            if left_child:  #if left_child != 0
                stack.append(left_child, curr_level + 1)
            


    return result
