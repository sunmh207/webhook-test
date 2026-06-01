def greet(name)
    if name = ""
        return "Hello, World!"
    else
        return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Python"))
