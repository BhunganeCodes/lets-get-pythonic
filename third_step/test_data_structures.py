import pytest
from data_structures_new import *
from unittest.mock import patch

# Question 1 - Matrix Transposer

@pytest.mark.parametrize("input_matrix, expected_output", [
    ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
    ([[1]], [[1]]),
    ([[1, 2], [3, 4], [5, 6]], [[1, 3, 5], [2, 4, 6]]),
    ([], []),
    ([[5, 10], [15, 20], [25, 30], [35, 40]], [[5, 15, 25, 35], [10, 20, 30, 40]]),
])
def test_matrix_transposer_logic(input_matrix, expected_output):
    assert matrix_transposer(input_matrix) == expected_output

def test_matrix_transposer_integrity():
    input_data = [[i, i+1, i+2] for i in range(1, 101)]
    result = matrix_transposer(input_data)
    
    assert len(result) == 3
    assert len(result[0]) == 100
    assert result[0][50] == 51

def test_matrix_transposer_invalid_shape():
    bad_input = [[1, 2], [3, 4, 5]]
    with pytest.raises(ValueError):
        matrix_transposer(bad_input)

def test_matrix_transposer_non_list_element():
    bad_input = [[1, 2], "not a list"]
    with pytest.raises(TypeError):
        matrix_transposer(bad_input)

def test_matrix_transposer_large_dataset():
    large_input = [[j for j in range(100)] for i in range(100)]
    result = matrix_transposer(large_input)
    assert len(result) == 100
    assert len(result[0]) == 100
    assert result[50][50] == 50

def test_matrix_transposer_square_matrix():
    assert matrix_transposer([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_matrix_transposer_rectangle_matrix():
    assert matrix_transposer([[1, 2, 3, 4], [5, 6, 7, 8]]) == [[1, 5], [2, 6], [3, 7], [4, 8]]

def test_matrix_transposer_single_row():
    assert matrix_transposer([[1, 2, 3, 4, 5]]) == [[1], [2], [3], [4], [5]]

def test_matrix_transposer_single_column():
    assert matrix_transposer([[1], [2], [3]]) == [[1, 2, 3]]

# ------------------------------------------------------------------------------------------ #

# Question 2 - Priority Queue Mapper

@pytest.mark.parametrize("tasks, expected_dict", [  
    ([("task1", 1), ("task2", 2), ("task3", 1)], {1: ["task1", "task3"], 2: ["task2"]}),    
    ([], {}),    
    ([("urgent", 3)], {3: ["urgent"]}),    
    ([("a", 1), ("b", 2), ("c", 1), ("d", 3)], {1: ["a", "c"], 2: ["b"], 3: ["d"]}),
])
def test_priority_queue_mapper_logic(tasks, expected_dict):
    assert priority_queue_mapper(tasks) == expected_dict

def test_priority_queue_mapper_duplicates():
    tasks = [("email", 2), ("call", 1), ("email", 2)]
    result = priority_queue_mapper(tasks)
    
    assert len(result[2]) == 2
    assert result[2] == ["email", "email"]

def test_priority_queue_mapper_large_scale():
    large_tasks = [(f"Task_{i}", i % 5) for i in range(100000)]
    result = priority_queue_mapper(large_tasks)
    
    assert len(result) == 5
    assert len(result[0]) == 20000

def test_priority_queue_mapper_invalid_tuple_size():
    bad_data = [("task1", 1), ("task2", 2, "extra")]
    with pytest.raises(ValueError):
        priority_queue_mapper(bad_data)

def test_priority_queue_mapper_non_integer_priority():
    bad_data = [("task1", "high")]
    with pytest.raises(TypeError):
        priority_queue_mapper(bad_data)

def test_priority_queue_mapper_single_task():
    assert priority_queue_mapper([('write_code', 5)]) == {5: ['write_code']}

def test_priority_queue_mapper_multiple_priorities():
    tasks = [('bug_fix', 1), ('feature', 3), ('refactor', 2), ('test', 1)]
    expected = {1: ['bug_fix', 'test'], 3: ['feature'], 2: ['refactor']}
    assert priority_queue_mapper(tasks) == expected

def test_priority_queue_mapper_negative_priorities():
    tasks = [('task_a', -1), ('task_b', 0), ('task_c', -1)]
    expected = {-1: ['task_a', 'task_c'], 0: ['task_b']}
    assert priority_queue_mapper(tasks) == expected

# ------------------------------------------------------------------------------------------ #

# Question 3 - Merge Sorted Lists

@pytest.mark.parametrize("list1, list2, expected_output", [
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
    ([], [1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [], [1, 2, 3]),
    ([], [], []),
    ([1], [2], [1, 2]),
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([5, 10, 15], [1, 7, 20], [1, 5, 7, 10, 15, 20]),
])
def test_merge_sorted_lists_logic(list1, list2, expected_output):
    assert merge_sorted_lists(list1, list2) == expected_output

def test_merge_sorted_lists_large_dataset():
    list1 = list(range(0, 10000, 2))
    list2 = list(range(1, 10000, 2))
    result = merge_sorted_lists(list1, list2)
    assert len(result) == 10000
    assert result == list(range(10000))

def test_merge_sorted_lists_unsorted_input():
    with pytest.raises(ValueError):
        merge_sorted_lists([3, 1, 2], [4, 5, 6])

def test_merge_sorted_lists_duplicates():
    assert merge_sorted_lists([1, 2, 3], [2, 3, 4]) == [1, 2, 2, 3, 3, 4]

def test_merge_sorted_lists_negative_numbers():
    assert merge_sorted_lists([-5, -2, 0], [-3, -1, 2]) == [-5, -3, -2, -1, 0, 2]

def test_merge_sorted_lists_same_elements():
    assert merge_sorted_lists([1, 1, 1], [1, 1, 1]) == [1, 1, 1, 1, 1, 1]

def test_merge_sorted_lists_one_empty():
    assert merge_sorted_lists([1, 5, 9], []) == [1, 5, 9]
    assert merge_sorted_lists([], [2, 4, 6]) == [2, 4, 6]

# ------------------------------------------------------------------------------------------ #

# Question 4 - Inventory Grouper

@pytest.mark.parametrize("products, expected", [
    (
        [ 
            {"sku": "A001", "category": "Electronics", "stock": 50}, 
            {"sku": "B002", "category": "Clothing", "stock": 30}, 
            {"sku": "A003", "category": "Electronics", "stock": 20}
        ],
        {"Electronics": {"total_stock": 70, "skus": ["A001", "A003"]}, "Clothing": {"total_stock": 30, "skus": ["B002"]}}
    ),
    (
        [
            {"sku": "X100", "category": "Books", "stock": 100},
            {"sku": "X101", "category": "Books", "stock": 50}
        ],
        {"Books": {"total_stock": 150, "skus": ["X100", "X101"]}}
    ),
    ([], {}),
    (
        [{"sku": "Z999", "category": "Toys", "stock": 10}],
        {"Toys": {"total_stock": 10, "skus": ["Z999"]}}
    ),
])
def test_inventory_grouper_logic(products, expected):
    assert inventory_grouper(products) == expected

def test_inventory_grouper_missing_keys():
    with pytest.raises(KeyError):
        inventory_grouper([{"sku": "A001", "category": "Electronics"}])

def test_inventory_grouper_non_dict_elements():
    with pytest.raises(TypeError):
        inventory_grouper([None])

def test_inventory_grouper_integrity():
    products = [{"sku": "TEST", "category": "Hardware", "stock": 5}]
    result = inventory_grouper(products)
    assert result["Hardware"]["total_stock"] == 5
    assert "TEST" in result["Hardware"]["skus"]

def test_inventory_grouper_large_input():
    products = [{"sku": f"SKU{i}", "category": "Tech", "stock": i} for i in range(1, 1001)]
    result = inventory_grouper(products)
    assert result["Tech"]["total_stock"] == sum(range(1, 1001))
    assert len(result["Tech"]["skus"]) == 1000

def test_inventory_grouper_multiple_categories():
    products = [        
        {'sku': 'FOOD1', 'category': 'Food', 'stock': 100},        
        {'sku': 'FOOD2', 'category': 'Food', 'stock': 50},        
        {'sku': 'DRINK1', 'category': 'Beverages', 'stock': 75}    
    ]
    expected_output = {        
        'Food': {'total_stock': 150, 'skus': ['FOOD1', 'FOOD2']},        
        'Beverages': {'total_stock': 75, 'skus': ['DRINK1']}    
    }
    assert inventory_grouper(products) == expected_output

def test_inventory_grouper_zero_stock():
    products = [{'sku': 'EMPTY', 'category': 'Other', 'stock': 0}]
    result = inventory_grouper(products)
    assert result["Other"]["total_stock"] == 0

# ------------------------------------------------------------------------------------------ #

# Question 5 - Paginator

@pytest.mark.parametrize("items, page_size, expected_output", [   
    (['A', 'B', 'C', 'D', 'E', 'F', 'G'], 3, [['A', 'B', 'C'], ['D', 'E', 'F'], ['G']]),    
    (['1', '2', '3', '4', '5', '6'], 2, [['1', '2'], ['3', '4'], ['5', '6']]),    
    ([], 5, []),    
    (['X'], 10, [['X']]),    
    (list(range(10)), 4, [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]),
])
def test_paginator_logic(items, page_size, expected_output):
    assert paginator(items, page_size) == expected_output

def test_paginator_immutability():
    original = ['A', 'B', 'C', 'D', 'E']
    original_copy = original.copy()
    
    paginator(original, 2)
    
    assert original == original_copy

def test_paginator_large_scale():
    large_input = list(range(100000))
    result = paginator(large_input, 1000)
    
    assert len(result) == 100
    assert len(result[0]) == 1000
    assert result[-1][-1] == 99999

def test_paginator_invalid_page_size():
    with pytest.raises(ValueError):
        paginator([1, 2, 3], 0)
    
    with pytest.raises(ValueError):
        paginator([1, 2, 3], -1)

def test_paginator_single_page():
    assert paginator([1, 2, 3], 5) == [[1, 2, 3]]

def test_paginator_exact_pages():
    assert paginator([1, 2, 3, 4, 5, 6], 3) == [[1, 2, 3], [4, 5, 6]]

def test_paginator_partial_last_page():
    assert paginator([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3], [4, 5, 6], [7]]

def test_paginator_page_size_one():
    assert paginator(['a', 'b', 'c'], 1) == [['a'], ['b'], ['c']]

def test_paginator_strings():
    items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    expected = [['apple', 'banana'], ['cherry', 'date'], ['elderberry']]
    assert paginator(items, 2) == expected

# ------------------------------------------------------------------------------------------ #

# Question 6 - Graph Degree Counter

@pytest.mark.parametrize("graph, expected_degrees", [
    (
        {"A": ["B", "C"], "B": ["A"], "C": ["A"]},
        {"A": 2, "B": 1, "C": 1}
    ),
    (
        {"X": ["Y", "Z"], "Y": ["X", "Z"], "Z": ["X", "Y"]},
        {"X": 2, "Y": 2, "Z": 2}
    ),
    ({}, {}),
    (
        {"Node1": [], "Node2": ["Node1"]},
        {"Node1": 0, "Node2": 1}
    ),
    (
        {"A": ["B", "C", "D"], "B": [], "C": [], "D": []},
        {"A": 3, "B": 0, "C": 0, "D": 0}
    )
])
def test_graph_degree_counter_logic(graph, expected_degrees):
    assert graph_degree_counter(graph) == expected_degrees

def test_graph_degree_counter_immutability():
    original = {"A": ["B"], "B": ["A"]}
    original_copy = {"A": ["B"], "B": ["A"]}
    graph_degree_counter(original)
    assert original == original_copy

def test_graph_degree_counter_non_iterable_value():
    with pytest.raises(TypeError):
        graph_degree_counter({"A": None})

def test_graph_degree_counter_large_graph():
    hub_graph = {"Hub": [f"Node{i}" for i in range(10000)]}
    for i in range(10000):
        hub_graph[f"Node{i}"] = []
    
    result = graph_degree_counter(hub_graph)
    assert result["Hub"] == 10000
    assert result["Node9999"] == 0

def test_graph_degree_counter_self_loop():
    self_loop = {"A": ["A"]}
    result = graph_degree_counter(self_loop)
    assert result == {"A": 1}

def test_graph_degree_counter_complete_graph():
    graph = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
    expected = {"A": 2, "B": 2, "C": 2}
    assert graph_degree_counter(graph) == expected

def test_graph_degree_counter_isolated_nodes():
    graph = {"A": [], "B": [], "C": []}
    expected = {"A": 0, "B": 0, "C": 0}
    assert graph_degree_counter(graph) == expected

# ------------------------------------------------------------------------------------------ #

# Question 7 - Factorial Calculator (Recursive)

@pytest.mark.parametrize("n, expected_output", [
    (0, 1),
    (1, 1),
    (2, 2),
    (5, 120),
    (10, 3628800),
    (7, 5040),
])
def test_factorial_calculator_logic(n, expected_output):
    assert factorial_calculator(n) == expected_output

def test_factorial_calculator_large_n():
    result = factorial_calculator(20)
    assert result == 2432902008176640000

def test_factorial_calculator_negative_n():
    with pytest.raises(ValueError):
        factorial_calculator(-5)

def test_factorial_calculator_non_integer_n():
    with pytest.raises(ValueError):
        factorial_calculator(5.5)

def test_factorial_calculator_integrity():
    assert factorial_calculator(3) == 6
    assert factorial_calculator(4) == 24
    assert factorial_calculator(6) == 720

def test_factorial_calculator_edge_cases():
    assert factorial_calculator(0) == 1
    assert factorial_calculator(1) == 1

def test_is_recursion_implemented():
    with patch("data_structures_new.factorial_calculator", wraps=factorial_calculator) as mocked_function:
        mocked_function(10)
        
        assert mocked_function.call_count > 1, f"Recursion not detected. Count: {mocked_function.call_count}"

def test_recursion_depth():
    depth = 2000
    with pytest.raises(RecursionError):
        factorial_calculator(depth)

def test_recursion_parameters():
    with patch("data_structures_new.factorial_calculator", wraps=factorial_calculator) as mocked_function:
        mocked_function(5)
        
        for call in mocked_function.call_args_list:
            args, _ = call
            assert len(args) == 1, "Recursive calls should have exactly one argument."
            assert isinstance(args[0], int), "Recursive call argument should be an integer."

def test_factorial_calculator_boundary():
    assert factorial_calculator(12) == 479001600
    assert factorial_calculator(15) == 1307674368000