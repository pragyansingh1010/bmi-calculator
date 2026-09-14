def rounded_bmi(weight, height):
    return round(weight / (height * height), 2)

assert rounded_bmi(70, 1.75) == 22.86
assert rounded_bmi(60, 1.6) == 23.44
assert rounded_bmi(80, 2) == 20
print('BMI rounding rules passed')
