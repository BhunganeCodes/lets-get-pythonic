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