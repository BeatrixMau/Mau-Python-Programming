import random

def print_health_quotes(random_number):
    health_quotes = [
        "Health is a state of complete harmony of the body, mind, and spirit. – B.K.S. Iyengar",
        "To keep the body in good health is a duty... otherwise, we shall not be able to keep our mind strong and clear. – Buddha",
        "The greatest wealth is health. – Virgil"
    ]

    if 1 <= random_number <= len(health_quotes):
        print(f"Random Health Quote {random_number}: {health_quotes[random_number - 1]}")
    else:
        print("Invalid random number. It should be between 1 and 3.")

random_number = random.randint(1, 3)
print_health_quotes(random_number)


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
def classify_obesity(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
weight = float(input("Enter Your Current Weight: "))
height = float(input ("Enter Your Current Height: "))

bmi_result = calculate_bmi(weight, height)
obesity_classification = classify_obesity(bmi_result)
print("Your BMI is:", bmi_result)
print("You are classified as:", obesity_classification)

