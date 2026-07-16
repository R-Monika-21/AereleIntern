"""
numbers = [int(i) for i in input("Enter numbers: ").split()]
squares = [i * i for i in numbers]
print(numbers)
print(squares)
"""
with open("Numbers.txt", "w") as file:
    numbers = [int(i) for i in input("Enter the numbers:").split()]
    for i in numbers:
        file.write(f"Number: {i}\n")