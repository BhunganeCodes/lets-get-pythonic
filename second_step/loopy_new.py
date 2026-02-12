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
    
    while True:
        password = input("Enter a password:")

        if re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&]).{8,}$", password):
            print("Strong password accepted!")
            break
        print("Too weak. Try again.")



def grade_analyzer(grades):
    if not grades:
        return "No Pass"
    
    for grade in grades:
        if grade < 60:
            return "No Pass"
    return "Pass"


def valley_finder(data):
    res = []

    for i in range(1, len(data) - 1):
        if data[i] < data[i - 1] and data[i] < data[i + 1]:
            res.append(data[i])
    return res


def email_validator(email_list):
    
    # TODO: Implement this function
    pass


def budget_tracker(budget, daily_expenses):
    
    # TODO: Implement this function
    # Simulate day by day, check for exceeding, balanced, or surplus
    pass