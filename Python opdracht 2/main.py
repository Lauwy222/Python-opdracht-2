from functools import wraps

# Definieer de decorator
def sum_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Print een bericht voor de functie-uitvoering
        print(f"Functie {func.__name__} wordt aangeroepen met args: {args} en kwargs: {kwargs}")
        # Voer de oorspronkelijke functie uit
        result = func(*args, **kwargs)
        # Print een bericht na de functie-uitvoering
        print(f"Functie {func.__name__} heeft geretourneerd: {result}")
        return result
    return wrapper

# Gebruik de decorator boven de functie
@sum_decorator
def sum_two_numbers(a, b):
    return a + b

# Testprogramma
if __name__ == "__main__":
    result = sum_two_numbers(69, 420)
    print(f"Resultaat: {result}")
