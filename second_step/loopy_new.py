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
print(temperature_converter([0, 100, -40]))

def password_strength():
    
    pass



def grade_analyzer(grades):
    pass


def valley_finder(data):
    pass


def email_validator(email_list):
    pass


def budget_tracker(budget, daily_expenses):
    pass