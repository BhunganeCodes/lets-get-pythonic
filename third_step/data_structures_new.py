def matrix_transposer(matrix):
    if not matrix:
        return []
    
    res = []
    for row in range(len(matrix[0])):
        temp = []
        for col in range(len(matrix)):
            if not isinstance(matrix[col], list):
                raise TypeError
            if len(matrix[col]) != len(matrix[0]):
                raise ValueError
            temp.append(matrix[col][row])
        res.append(temp)
    return res


def priority_queue_mapper(tasks):
    
    # TODO: Implement this function
    # Hint: Use setdefault() or defaultdict
    pass


def merge_sorted_lists(list1, list2):

    if list1 != sorted(list1) or list2 != sorted(list2):
        raise ValueError
    
    res = []
    res.extend(list1)
    res.extend(list2)
    return sorted(res)
    

def inventory_grouper(products):
    
    # TODO: Implement this function
    # Hint: Use nested dictionaries, accumulate totals
    pass


def paginator(items, page_size):
    
    # TODO: Implement this function
    # Hint: Use list slicing in a loop
    pass


def graph_degree_counter(graph):
    
    # TODO: Implement this function
    # Hint: Simply count length of each adjacency list
    pass


def factorial_calculator(n):
    
    # TODO: Implement this function using RECURSION
    # Base case: if n == 0 or n == 1, return 1
    # Recursive case: return n * factorial_calculator(n - 1)
    pass