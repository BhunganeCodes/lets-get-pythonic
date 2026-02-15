import re

def recipe_scaler(ingredients, multiplier):
    res = []

    for item in ingredients:
        res.append(item * multiplier)
    
    return res


def temperature_converter(celsius_temps):
    if not celsius_temps:
        return []

    res = []

    for c in celsius_temps:
        res.append(int(c * 9/5) + 32)
    
    return res


def password_strength():
    special_chars = "!@#$%^&*"
    
    while True:
        password = input("Enter a password:")

        uppercase = any(char.isupper for char in password)
        numeric = any(char.isdigit() for char in password)
        lowercase = any(char.islower() for char in password)
        special = any(char for char in password if char in special_chars)

        if uppercase and numeric and lowercase and special:
            print("Strong password accepted!")
            break
        print("Too weak. Try again.")


def grade_analyzer(grades):
    if not grades:
        return "No Pass"

    for g in grades:
        if g < 60:
            return "No Pass"
    
    return "Pass"


def valley_finder(data):
    res = []

    for i in range(1, len(data) - 1):
        if data[i] < data[i-1] and data[i] < data[i+1]:
            res.append(data[i])
    
    return res


def email_validator(email_list):
    pass


def budget_tracker(budget, daily_expenses):
    
    for day, exp in enumerate(daily_expenses, start=1):
        budget -= exp

        if budget < 0:
            return f"Budget exceeded on day {day}!"

    if budget > 0:
        return f"Budget surplus: R {budget}"
    return "Budget balanced perfectly!"