numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)


new_numbers = [4, 52, 3, 9, 7]
print(sorted(new_numbers))  # this will not modify the list
print(new_numbers)

print(sorted(new_numbers, reverse=True))
print(new_numbers)
