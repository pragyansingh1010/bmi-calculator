def valid_bmi_input(height, weight):
    return height > 0 and weight > 0

assert valid_bmi_input(1.75, 70)
assert not valid_bmi_input(0, 70)
assert not valid_bmi_input(1.75, 0)
assert not valid_bmi_input(-1.75, 70)
print('BMI input rules passed')
