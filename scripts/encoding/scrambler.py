source = "110100011100000011000000"
encoded = ""
index = 0


def get_bit(index, str):
    if index < 0:
        return 0
    return 1 if str[index] == "1" else 0


def scramble_bit(index):
    return get_bit(index, source) ^ get_bit(index - 5, encoded) ^ get_bit(index - 7, encoded)


for it in range(len(source)):
    bit = scramble_bit(it)
    encoded += "1" if bit == 1 else "0"

print("Source: ", source)
print("Encoded:", encoded)

print("Latex formula:")
print(" === ")
print("$$")
print("\\begin{array}{lllllll}")
for it in range(len(source)):
    if it > 7:
        print("    " "A_{" f"{it + 1}" "} = " f"{source[it]} " "& & B_{" f"{it + 1}" "} & = & A_" "{" f"{it + 1}" "} \\oplus B_{" f"{it + 1 - 5}" "} \\oplus B_{" f"{it + 1 - 7}" "} & = & " f"{encoded[it]} \\\\")
    elif it > 5:
        print("    " "A_{" f"{it + 1}" "} = " f"{source[it]} " "& & B_{" f"{it + 1}" "} & = & A_" "{" f"{it + 1}" "} \\oplus B_{" f"{it + 1 - 5}" "} & = & " f"{encoded[it]} \\\\")
    else:
        print("    " "A_{" f"{it + 1}" "} = " f"{source[it]} " f"& & B_{it + 1} & = & A_{it + 1} & = & {encoded[it]} \\\\")
print("\\end{array}")
print("$$")
print(" === ")
