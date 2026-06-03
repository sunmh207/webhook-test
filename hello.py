def greet(name: str) -> str:
    """Return a greeting for the given name.

    Returns "Hello, World!" when name is empty, otherwise "Hello, {name}!".
    """
    if name == "":
        return "Hello, World!"
    else:
        return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("Python"))
