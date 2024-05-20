# Definieer de decorator-functie
def sum_decorator(func):
    def wrapper(*args, **kwargs):
        print("before execution")
        result = func(*args, **kwargs)
        print("after execution")
        return result
    return wrapper

# Pas de decorator toe op de functie sum_two_numbers
@sum_decorator
def sum_two_numbers(a, b):
    print("inside the function")
    return a + b

# Testprogramma
a, b = 123, 456
print("sum =", sum_two_numbers(a, b))
