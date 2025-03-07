
decimal = int(input("Enter Decimal Number"))
temp_dec = decimal
octal = 0
i = 0
while (temp_dec > 0):
    remainder = temp_dec % 8
    temp_dec //= 8
    octal += (10 ** i) * remainder
    i += 1

print(octal)
