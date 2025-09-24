# Can't run the code for whatever reason, testing in powershell lmfao
def divide_numbers(a: int | float, b: int | float) -> float:
    a, b = float(a), float(b)
    try: 
        return a / b 
    except ZeroDivisionError: 
        return float('inf')

divide_numbers(7, "10")
