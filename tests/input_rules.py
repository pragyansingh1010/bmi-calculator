def valid_input(value):
    return isinstance(value, (int, float)) and value > 0

assert valid_input(1)
assert valid_input(70.5)
assert not valid_input(0)
assert not valid_input(-2)
print('BMI input rules passed')
