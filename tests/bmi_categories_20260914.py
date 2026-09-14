def category(value):
    if value < 18.5: return 'underweight'
    if value < 25: return 'normal'
    if value < 30: return 'overweight'
    return 'obese'

assert category(18) == 'underweight'
assert category(22) == 'normal'
assert category(27) == 'overweight'
assert category(32) == 'obese'
print('BMI categories passed')
