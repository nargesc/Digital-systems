def hex_to_binary(hex_number, bits):

    binary_rep = bin(int(hex_number, 16))[2:]  # Remove the '0b' prefix


    if len(binary_rep) > bits:
        return f"Not possible to fit into {bits} bits"
    else:

        return binary_rep.zfill(bits)


def binary_to_binary(binary_number, bits):

    if len(binary_number) > bits:
        return f"Not possible to fit into {bits} bits"
    else:

        return binary_number.zfill(bits)


# a) 0x1E5 → 8 bit binary
hex_a = "0x1E5"
result_a = hex_to_binary(hex_a, 8)

# b) 0x0F1 → 8 bit binary
hex_b = "0x0F1"
result_b = hex_to_binary(hex_b, 8)

# c) 0x2E8 → 10 bit binary
hex_c = "0x2E8"
result_c = hex_to_binary(hex_c, 10)

# d) 0000 0100 1000 1011 → 12 bit binary
binary_d = "0000010010001011"
result_d = binary_to_binary(binary_d, 12)

# e) 1101 1001 → 16 bit binary
binary_e = "11011001"
result_e = binary_to_binary(binary_e, 16)

# Display results
print(f"a) {hex_a} → 8 bit binary: {result_a}")
print(f"b) {hex_b} → 8 bit binary: {result_b}")
print(f"c) {hex_c} → 10 bit binary: {result_c}")
print(f"d) {binary_d} → 12 bit binary: {result_d}")
print(f"e) {binary_e} → 16 bit binary: {result_e}")
