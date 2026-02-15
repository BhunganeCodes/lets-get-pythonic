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
    
    pass



def grade_analyzer(grades):
    if not grades:
        return "No Pass"

    for g in grades:
        if g < 60:
            return "No Pass"
    
    return "Pass"


def valley_finder(data):
    pass


def email_validator(email_list):
    pass


def budget_tracker(budget, daily_expenses):
    pass