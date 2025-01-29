hex_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

num_bytes = len(hex_str)//2

hex_int = int(hex_str, base=16)

# Brute force through A-Z
for c in range(ord("A"), ord("Z")+1):
    # Generate num_bytes length hex number of c
    key_int = 0
    for num in range(num_bytes):
        key_int += (c << 8*num)

    xor_out_int = hex_int ^ key_int
    xor_out_hex = hex(xor_out_int)
    xor_out_str = str(xor_out_hex)[2:]

    # Convert each byte to a character
    msg_str = ""
    for num in range(num_bytes):
        hex_dig = xor_out_str[2*num:2*num+2]
        hex_dig_int = int(hex_dig, base=16)

        msg_str += chr(hex_dig_int)
    print(f'Using character {chr(c)}: {msg_str}')
