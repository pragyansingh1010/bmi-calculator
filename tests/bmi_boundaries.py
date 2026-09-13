def bmi(weight, height):
    return weight / (height * height)

assert round(bmi(70, 1.75), 2) == 22.86
assert bmi(50, 2) > 0
assert bmi(80, 2) == 20
print("BMI calculation tests passed")
