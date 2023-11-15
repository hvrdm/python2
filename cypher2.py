import sys

def caesar_encrypt(text, shift):
    shift = shift % 26  # Sørger for at shift-verdien ruller rundt ved verdier over 25
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(table)

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# Testkoden
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Bruk: python cypher.py 'Tekst jeg vil kryptere' <forskyvning>")
        sys.exit(1)

    original_text = sys.argv[1]
    shift_amount = int(sys.argv[2])

    encrypted = caesar_encrypt(original_text, shift_amount)
    print("Kryptert tekst:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift_amount)
    print("Dekryptert tekst:", decrypted)
