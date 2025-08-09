#belajar func atau define a func

def say_hello():
    print("Hello, World!")

# Memanggil fungsi
say_hello()

def greet(name):
    print(f"Hello, {name}!")

# Memanggil fungsi dengan memberikan argumen
greet("Will")
greet("Jo")

def add(a, b):
    return a + b

result = add(5, 3)
print(result)

def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(result)

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Tidak memberikan argumen
greet("Alice")  # Memberikan argumen

def sum_all(*numbers):
    return sum(numbers)

result = sum_all(1, 2, 3, 4, 5)
print(result)

def do_nothing():
    return

result = do_nothing()
print(result)

