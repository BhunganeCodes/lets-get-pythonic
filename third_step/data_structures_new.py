def matrix_transposer(matrix):
    if not matrix:
        return []
    
    first_row = matrix[0]

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError
        
        if len(row) != len(first_row):
            raise ValueError
    
    res = []

    for col in range(len(first_row)):
        temp = []
        for row in range(len(matrix)):
            temp.append(matrix[row][col])
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
    
    return sorted(list1 + list2)
    

def inventory_grouper(products):
    res = {}
    
    for item in products:
        if len(item) != 3:
            raise KeyError
        
        category = item["category"]
        sku = item["sku"]
        stock = item["stock"]

        
        if category not in res:
            res[category] = {"total_stock": 0, "skus": []}
        
        res[category]["total_stock"] += stock
        res[category]["skus"].append(sku)

    return res


def paginator(items, page_size):

    if page_size < 1:
        raise ValueError

    res = []

    for i in range(0, len(items), page_size):
        res.append(items[i:i+page_size])
    
    return res


def graph_degree_counter(graph):
    
    if not graph:
        return {}

    res = {}
    
    for k, v in graph.items():
        res[k] = len(v)
    
    return res


def factorial_calculator(n):

    if n < 0:
        raise ValueError
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_calculator(n - 1)