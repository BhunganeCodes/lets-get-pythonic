from io import StringIO
import first_step.fundamentals as fun_ext
import sys

class TestExtendedFunctions():
    
    def test_fizzbuzz_function_exists(self):
        assert callable(getattr(fun_ext, 'fizzbuzz', None)), \
            "Function 'fizzbuzz' is not defined"


    def test_fizzbuzz_output(self): 
        test_cases = [
            (15, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']),
            (5, ['1', '2', 'Fizz', '4', 'Buzz']),
            (3, ['1', '2', 'Fizz']),
            (10, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']),
        ]
        
        for n, expected_output in test_cases:
            captured_output = StringIO() 
            sys.stdout = captured_output 
            fun_ext.fizzbuzz(n) 
            sys.stdout = sys.__stdout__ 
            output = captured_output.getvalue().strip().split('\n') 
            assert output == expected_output, (
                f"Function 'fizzbuzz({n})' does not produce the expected output. Expected {expected_output}, got {output}")


    def test_count_vowels_function_exists(self):
        assert callable(getattr(fun_ext, 'count_vowels', None)), \
            "Function 'count_vowels' is not defined"


    def test_count_vowels_returns_correctly(self): 
        test_cases = [
            ("hello", 2),
            ("AEIOU", 5),
            ("Python Programming", 4),
            ("rhythm", 0),
            ("Education", 5),
            ("", 0),
            ("bcdfg", 0),
            ("The quick brown fox", 5),
        ]

        for text, expected in test_cases:
            result = fun_ext.count_vowels(text)
            assert result == expected, \
                f"Function 'count_vowels(\"{text}\")' should return {expected}, got {result}"
    

    def test_is_palindrome_function_exists(self):
        assert callable(getattr(fun_ext, 'is_palindrome', None)), \
            "Function 'is_palindrome' is not defined"


    def test_is_palindrome_returns_correctly(self):
        test_cases = [
            ("racecar", True),
            ("hello", False),
            ("A man a plan a canal Panama", True),
            ("Was it a car or a cat I saw", True),
            ("Python", False),
            ("Madam", True),
            ("", True),
            ("a", True),
            ("ab", False),
        ]

        for text, expected in test_cases:
            result = fun_ext.is_palindrome(text)
            assert result == expected, \
                f"Function 'is_palindrome(\"{text}\")' should return {expected}, got {result}"


    def test_find_max_function_exists(self):
        assert callable(getattr(fun_ext, 'find_max', None)), \
            "Function 'find_max' is not defined"


    def test_find_max_returns_correctly(self):
        test_cases = [
            ([1, 5, 3, 9, 2], 9),
            ([10], 10),
            ([-5, -2, -10, -1], -1),
            ([0, 0, 0], 0),
            ([100, 200, 50, 75], 200),
            ([7, 3, 9, 2, 8, 9, 1], 9),
        ]

        for numbers, expected in test_cases:
            result = fun_ext.find_max(numbers)
            assert result == expected, \
                f"Function 'find_max({numbers})' should return {expected}, got {result}"


    def test_find_max_empty_list(self):
        result = fun_ext.find_max([])
        assert result is None, \
            f"Function 'find_max([])' should return None for empty list, got {result}"


    def test_calculate_average_function_exists(self):
        assert callable(getattr(fun_ext, 'calculate_average', None)), \
            "Function 'calculate_average' is not defined"


    def test_calculate_average_returns_correctly(self):
        test_cases = [
            ([10, 20, 30], 20.0),
            ([5, 5, 5, 5], 5.0),
            ([1, 2, 3, 4, 5], 3.0),
            ([100], 100.0),
            ([10, 15, 20, 25, 30], 20.0),
            ([-10, 0, 10], 0.0),
        ]

        for numbers, expected in test_cases:
            result = fun_ext.calculate_average(numbers)
            assert result == expected, \
                f"Function 'calculate_average({numbers})' should return {expected}, got {result}"


    def test_calculate_average_empty_list(self):
        result = fun_ext.calculate_average([])
        assert result == 0, \
            f"Function 'calculate_average([])' should return 0 for empty list, got {result}"


    def test_remove_duplicates_function_exists(self):
        assert callable(getattr(fun_ext, 'remove_duplicates', None)), \
            "Function 'remove_duplicates' is not defined"


    def test_remove_duplicates_returns_correctly(self):
        test_cases = [
            ([1, 2, 2, 3, 4, 4, 5], [1, 2, 3, 4, 5]),
            ([1, 1, 1, 1], [1]),
            ([5, 4, 3, 2, 1], [5, 4, 3, 2, 1]),
            ([], []),
            ([10], [10]),
            ([1, 2, 1, 3, 2, 4, 3, 5], [1, 2, 3, 4, 5]),
        ]

        for numbers, expected in test_cases:
            result = fun_ext.remove_duplicates(numbers)
            assert result == expected, \
                f"Function 'remove_duplicates({numbers})' should return {expected}, got {result}"


    def test_multiplication_table_function_exists(self):
        assert callable(getattr(fun_ext, 'multiplication_table', None)), \
            "Function 'multiplication_table' is not defined"


    def test_multiplication_table_output(self):
        test_cases = [
            (3, ['1 x 3 = 3', '2 x 3 = 6', '3 x 3 = 9', '4 x 3 = 12', '5 x 3 = 15', 
                 '6 x 3 = 18', '7 x 3 = 21', '8 x 3 = 24', '9 x 3 = 27', '10 x 3 = 30']),
            (5, ['1 x 5 = 5', '2 x 5 = 10', '3 x 5 = 15', '4 x 5 = 20', '5 x 5 = 25',
                 '6 x 5 = 30', '7 x 5 = 35', '8 x 5 = 40', '9 x 5 = 45', '10 x 5 = 50']),
            (1, ['1 x 1 = 1', '2 x 1 = 2', '3 x 1 = 3', '4 x 1 = 4', '5 x 1 = 5',
                 '6 x 1 = 6', '7 x 1 = 7', '8 x 1 = 8', '9 x 1 = 9', '10 x 1 = 10']),
        ]

        for n, expected_output in test_cases:
            captured_output = StringIO()
            sys.stdout = captured_output
            fun_ext.multiplication_table(n)
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue().strip().split('\n')
            assert output == expected_output, \
                f"Function 'multiplication_table({n})' does not print correctly. Expected {expected_output}, got {output}"