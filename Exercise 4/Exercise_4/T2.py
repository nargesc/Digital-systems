def decimal_to_twos_complement(n, bits=8):

    if n >= 0:

        return format(n, f"0{bits}b")


    else:

        n = abs(n)

        binary = format(n, f"0{bits}b")


        inverted = ''.join('1' if bit == '0' else '0' for bit in binary)


        result = bin(int(inverted, 2) + 1)[2:].zfill(bits)

        return result



numbers = [59, -1,-128, -97]
twos_complement_numbers = {num: decimal_to_twos_complement(num) for num in numbers}

# Print the results
for num, twos_complement in twos_complement_numbers.items():
    print(f"{num} in two's complement using 8 bits: {twos_complement}")
