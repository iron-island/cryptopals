hex_str1 = "1c0111001f010100061a024b53535009181c"
hex_str2 = "686974207468652062756c6c277320657965"

exp_xor_out_hex_str = "746865206b696420646f6e277420706c6179"

hex_int1 = int(hex_str1, base=16)
hex_int2 = int(hex_str2, base=16)

xor_out_int = hex_int1 ^ hex_int2
act_xor_out_hex_str = hex(xor_out_int)[2:]

assert(act_xor_out_hex_str == exp_xor_out_hex_str)

print(f'Hex string 1             : {hex_str1}')
print(f'Hex string 2             : {hex_str2}')
print("")
print(f'Expected XORed hex string: {exp_xor_out_hex_str}')
print(f'Actual   XORed hex string: {act_xor_out_hex_str}')
