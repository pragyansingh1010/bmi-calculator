def category(value):
    if value < 18.5: return 'underweight'
    if value < 25: return 'normal'
    if value < 30: return 'overweight'
    return 'obese'

assert category(18.4) == 'underweight'
assert category(18.5) == 'normal'
assert category(25) == 'overweight'
assert category(30) == 'obese'
print('BMI category boundaries passed')
