#function that returns the result of a^b
def power_recursive(a,b):
    if b == 0:
        return 1
    else:
        return a * power_recursive(a,b-1)
print(power_recursive(2,3))

def power_iterative(a,b):
    result = 1
    for i in range(b):
        result *= a
    return result
print(power_iterative(2,3))
