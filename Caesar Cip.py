def shift_symbol(symbol, key):
    if symbol.isalpha():
        start = ord('A') if symbol.isupper() else ord('a')
        shifted = (ord(symbol) - start + key) % 26 + start
        return chr(shifted)
    else:
        return symbol
    
def caesar_cip(message, key):
    result = ""
    for symbol in message:
        result += shift_symbol(symbol, key)
    return result

print("Welcome to Caesar Cipher!")
mode = input("Do you want to encrypt or decrypt? ").strip().lower()
while mode not in ["encrypt", "decrypt"]:
    mode = input("Please type 'encrypt' or 'decrypt'? ").strip().lower()
message = input("Enter yout message:")
key = int(input("enter a key(1 - 26):"))
while not(1 <=key <= 26):
    key = int(input("Invalid type. Enter a number between 1 - 26."))
if mode == "decrypt":
    key = -key
output = caesar_cip(message, key)
print("\nYour result:")
print(output)