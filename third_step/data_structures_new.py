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
    res = {}

    for tsk in tasks:
        if len(tsk)!= 2:
            raise ValueError
        task, priority = tsk
        if not isinstance(priority, int):
            raise TypeError
        if priority not in res:
            res[priority] = [task]
        else:
            res[priority].append(task)
    return res
    

def merge_sorted_lists(list1, list2):

    if list1 != sorted(list1) or list2 != sorted(list2):
        raise ValueError
    
    res = []
    res.extend(list1)
    res.extend(list2)
    return sorted(res)
    

def inventory_grouper(products):
    res = {}
    for item in products:
        temp = {}
        for k, v in item.items():
            if isinstance(v, str) and v.isalnum():
                if v not in temp:
                    temp["skus"] = [v]
                    print(temp)


   

def paginator(items, page_size):
    if page_size < 1:
        raise ValueError
    
    res = []

    while items:
        res.append(items[:page_size])
        del items[:page_size]
    return res


def graph_degree_counter(graph):
    
    # TODO: Implement this function
    # Hint: Simply count length of each adjacency list
    pass


def factorial_calculator(n):
    
    # TODO: Implement this function using RECURSION
    # Base case: if n == 0 or n == 1, return 1
    # Recursive case: return n * factorial_calculator(n - 1)
    pass