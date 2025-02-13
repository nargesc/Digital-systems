def decimal_to_binary(decimal_number):
    if decimal_number >= 0:
        return bin(decimal_number)[2:]  # Remove the '0b' prefix
    else:
        return '-' + bin(decimal_number)[3:]  # Handle negative numbers

# Example usage
decimal_number = 55
binary_number = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is {binary_number}")
