import random

numbers = [random.randint(-100, 100) for _ in range(20)]
print("List of numbers:", numbers)

sum_of_negatives = sum([num for num in numbers if num < 0])

sum_of_evens = sum([num for num in numbers if num % 2 == 0])

sum_of_odds = sum([num for num in numbers if num % 2 != 0])

product_of_multiples_of_3 = 1
for i in range(0, len(numbers), 3):
    product_of_multiples_of_3 *= numbers[i]

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
if min_index > max_index:
    min_index, max_index = max_index, min_index
product_between_min_max = 1
for num in numbers[min_index+1:max_index]:
    product_between_min_max *= num

first_positive_index = next((i for i, num in enumerate(numbers) if num > 0), None)
last_positive_index = next((i for i, num in enumerate(reversed(numbers)) if num > 0), None)
if last_positive_index is not None:
    last_positive_index = len(numbers) - 1 - last_positive_index
sum_between_positives = sum(numbers[first_positive_index+1:last_positive_index])

print("\nResults:")
print("Sum of negative numbers:", sum_of_negatives)
print("Sum of even numbers:", sum_of_evens)
print("Sum of odd numbers:", sum_of_odds)
print("Product of numbers with indices multiples of 3:", product_of_multiples_of_3)
print("Product of numbers between min and max:", product_between_min_max)
print("Sum of numbers between the first and last positive numbers:", sum_between_positives)
