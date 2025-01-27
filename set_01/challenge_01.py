def int_to_base64(int_6b: int):
    # Base64 encoding:
    # 00 to 25: A to Z
    # 26 to 51: a to z
    # 52 to 61: 0 to 9
    # 62: +
    # 63: /

    if (0 <= int_6b <= 25):
        base64_char = chr(ord("A") + int_6b)
    elif (26 <= int_6b <= 51):
        base64_char = chr(ord("a") + int_6b - 26)
    elif (52 <= int_6b <= 61):
        base64_char = chr(ord("0") + int_6b - 52)
    elif (int_6b == 62):
        base64_char = "+"
    elif (int_6b == 63):
        base64_char = "/"

    return base64_char

hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

exp_base64_str = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

actual_str = str(bytes.fromhex(hex_str))
print(actual_str)

# Convert hex string 3 digits at a time to generate 2 base64 digits

# Left pad with zeros if hex string is not divisible by 3 hex digits
if (len(hex_str) % 3 != 0):
    leftpad = len(hex_str) % 3
    hex_str = "0"*leftpad + hex_str

actual_base64_str = ""
for i in range(len(hex_str)//3):
    hex_dig2 = int(hex_str[3*i], base=16)
    hex_dig1 = int(hex_str[3*i+1], base=16)
    hex_dig0 = int(hex_str[3*i+2], base=16)

    int_6b_upper = (hex_dig2 << 2) + (hex_dig1 >> 2)
    int_6b_lower = ((hex_dig1 & 0x3) << 4) + hex_dig0

    actual_base64_str += int_to_base64(int_6b_upper) + int_to_base64(int_6b_lower)

print(f'Expected: {exp_base64_str}')
print(f'Actual  : {actual_base64_str}')
assert(actual_base64_str == exp_base64_str)
