import hashlib

def verify_hash(file_path, hash_file_path):
    """Verifiserer at den genererte SHA-256 hash for filen matcher den lagrede hash-verdien."""
    try:
        # Les den lagrede hashverdien og fjern whitespace
        with open(hash_file_path, 'r') as hash_file:
            original_hash = hash_file.read().strip()

        # Initialiser hash generator
        sha256_hash = hashlib.sha256()
        
        # Åpne den angitte filen og kalkuler dens hash
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        
        # Kalkuler den endelige hashverdien og sammenlign den
        file_hash = sha256_hash.hexdigest()
        if file_hash == original_hash:
            print(f"Hash-verdien matcher for filen {file_path}. Filen er uendret.")
        else:
            print(f"Hash-verdien matcher ikke for filen {file_path}. Filen kan være endret.")

    except FileNotFoundError:
        print(f"Filen '{file_path}' eller '{hash_file_path}' ble ikke funnet.")
    except Exception as e:
        print(f"En feil oppstod: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Bruk: python hash_verifier.py [filsti] [hash-filsti]")
    else:
        file_path = sys.argv[1]
        hash_file_path = sys.argv[2]
        verify_hash(file_path, hash_file_path)
