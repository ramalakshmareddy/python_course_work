n = int(input("Enter a number: "))
product = 1

while n > 0:
    digit = n % 10         # Extract the last digit
    product *= digit       # Multiply with product
    n = n // 10            # Remove the last digit

print("Product of digits:", product)
