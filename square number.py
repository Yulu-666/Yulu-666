def int_sqrt(n):
    for m in range(n+1):
        if m * m == n:
            return m
    raise ValueError(f"{n} is not square number!")

def safe_int_sqrt(n):
    try:
        result = int_sqrt(n)
        print(f"The integer root of {n} is {result}")
    except ValueError as e:
        print("Error", e)
    finally:
        print("End of computation.\n")
        
safe_int_sqrt(9)