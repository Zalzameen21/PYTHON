def is_even(num):
    return all(int(digit) % 2 == 0 for digit in str(num))

even_squares = [num for num in range(1000, 10000) if is_even(num) and int(num**0.5) ** 2 == num]
print(even_squares)
