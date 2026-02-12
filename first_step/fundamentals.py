def fizzbuzz(n):
    
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(f"{i}")


def count_vowels(text):
    
    count = 0
    vowels = "aeiouAEIOU"

    for char in text:
        if char in vowels:
            count += 1
    return count


def is_palindrome(text):
    
    text = text.replace(" ", "").lower()

    return text == text[::-1]


def find_max(numbers):
    if not numbers:
        return None
    res = numbers[0]

    for num in numbers:
        if num > res:
            res = num
    return res


def calculate_average(numbers):
    if not numbers:
        return 0
    
    return sum(numbers) / len(numbers)


def remove_duplicates(numbers):
    
    res = []

    for num in numbers:
        if num in res:
            continue
        res.append(num)
    return res


def multiplication_table(n):
    
    # TODO: Implement this function
    pass