#belajar break & looping (for, while)

while True: #kondisi terpenuhi
    user_input = input("Type 'exit' to quit: ")
    if user_input.lower() == 'loop':  # Menghentikan loop jika pengguna mengetik 'exit'
        print("loop.")
    elif user_input.lower()== 'exit':
        print("You typed:", user_input)
        break
    else:
        print("Out from loop")

for counter in range(0,10):
    print(f"This is for loop number {counter+1}")

for i in range(0, 10):
    print(i)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
