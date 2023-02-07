for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
cubes = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    cubes.append(value ** 3)

print(squares)
print(cubes)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"min(digits): {min(digits)}")
print(f"max(digits): {max(digits)}")
print(f"sum(digits): {sum(digits)}")

quads = [value**4 for value in range(1, 11)]
print(quads)