def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print(greet("World"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"Fibonacci(10) = {fibonacci(10)}")
