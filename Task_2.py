import random

numbers = [random.randint(-100, 100) for _ in range(20)]
print("Original list:", numbers)

even_numbers = [num for num in numbers if num % 2 == 0]

odd_numbers = [num for num in numbers if num % 2 != 0]

negative_numbers = [num for num in numbers if num < 0]

positive_numbers = [num for num in numbers if num > 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Negative numbers:", negative_numbers)
print("Positive numbers:", positive_numbers)
