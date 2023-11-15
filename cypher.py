import sys

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

def caesar_crack(ciphertext):
    FREQUENT_CHARS = "etaoinshrdlu"
    best_shift = 0
    max_char_match = 0
    for possible_shift in range(26):
        decrypted_test = caesar_decrypt(ciphertext, possible_shift)
        char_match = sum(char in FREQUENT_CHARS for char in decrypted_test.lower())
        if char_match > max_char_match:
            max_char_match = char_match
            best_shift = possible_shift
    return caesar_decrypt(ciphertext, best_shift)

# Hovedprogram som håndterer kommandolinjeargumenter
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Bruk: python cypher.py 'Tekst jeg vil kryptere' <forskyvning>")
        sys.exit(1)

    text_to_encrypt = sys.argv[1]
    shift_value = int(sys.argv[2])

    encrypted = caesar_encrypt(text_to_encrypt, shift_value)
    print("Kryptert tekst:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift_value)
    print("Dekryptert tekst:", decrypted)
