def bmi(weight, height):
    return weight / (height * height)

assert round(bmi(70, 1.75), 2) == 22.86
assert round(bmi(100, 2), 2) == 25
assert round(bmi(50, 1.5), 2) == 22.22
print('BMI formula rules passed')
