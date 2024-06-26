# Expansion P-box Table
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

def permute(block, table):
    """
    Permute the input block using the specified table.
    """
    return ''.join([block[table[i] - 1] for i in range(len(table))])

def hex_to_bin(hex_string):
    """
    Convert a hex string to a binary string.
    """
    return bin(int(hex_string, 16))[2:].zfill(32)

def bin_to_hex(bin_string):
    """
    Convert a binary string to a hex string.
    """
    return hex(int(bin_string, 2))[2:].upper().zfill(12)

def main():
    # Example 32-bit block (in hexadecimal)
    hex_input = input("Enter an 8-character hexadecimal value: ").strip()
    print(f"Input (hex): {hex_input}")

    # Convert hex input to binary
    bin_input = hex_to_bin(hex_input)
    print(f"Input (binary): {bin_input}")

    # Apply expansion permutation
    exp_output = permute(bin_input, E)
    print(f"After Expansion Permutation (binary): {exp_output}")
    print(f"After Expansion Permutation (hex): {bin_to_hex(exp_output)}")

if __name__ == "__main__":
    main()