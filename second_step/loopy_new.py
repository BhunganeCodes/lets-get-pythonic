import re


def recipe_scaler(ingredients, multiplier):
    res = []

    for item in ingredients:
        res.append(int(item * multiplier))
    return res


def temperature_converter(celsius_temps):
    res = []

    for c in celsius_temps:
        res.append(int(c * 9/5) + 32)
    return res


def password_strength():
    
    # TODO: Implement this function
    # Use while loop and input() to get user input
    pass


def grade_analyzer(grades):
    
    # TODO: Implement this function
    pass


def valley_finder(data):
    
    # TODO: Implement this function
    # Remember: edges cannot be valleys, must be STRICTLY lower
    pass


def email_validator(email_list):
    
    # TODO: Implement this function
    pass


def budget_tracker(budget, daily_expenses):
    
    # TODO: Implement this function
    # Simulate day by day, check for exceeding, balanced, or surplus
    pass