def hex_to_binary(hex_number, bits):

    binary_rep = bin(int(hex_number, 16))[2:]  # Remove '0b' prefix

    if len(binary_rep) > bits:
        return f"Not possible to fit into {bits} bits"
    else:

        return binary_rep.zfill(bits)

def two_complement_conversion(binary_number, bits):

    if binary_number[0] == '1':  # Negative number
        return binary_number.zfill(bits)
    else:
        return binary_number.zfill(bits)

def binary_to_binary(binary_number, bits):

    if len(binary_number) > bits:
        return f"Not possible to fit into {bits} bits"
    else:
        return binary_number.zfill(bits)

# a) 1001 1101₂ → 12 bit binary
binary_a = "10011101"
result_a = two_complement_conversion(binary_a, 12)

# b) 1110 1011 1001 0001₂ → 12 bit binary
binary_b = "1110101110010001"
result_b = binary_to_binary(binary_b, 12)

# c) 0xFAC → 16 bit binary
hex_c = "0xFAC"
result_c = hex_to_binary(hex_c, 16)

# d) 0xFF13 → 10 bit binary
hex_d = "0xFF13"
result_d = hex_to_binary(hex_d, 10)

# Display results
print(f"a) {binary_a} → 12 bit binary: {result_a}")
print(f"b) {binary_b} → 12 bit binary: {result_b}")
print(f"c) {hex_c} → 16 bit binary: {result_c}")
print(f"d) {hex_d} → 10 bit binary: {result_d}")
