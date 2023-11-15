import hashlib

def generate_hash(file_path):
    """Genererer SHA-256 hash for den angitte filen."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Les filen i små biter for å håndtere store filer
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        hash_value = sha256_hash.hexdigest()
        print(f"SHA-256 hash for filen {file_path} er: {hash_value}")
        return hash_value
    except FileNotFoundError:
        print(f"Filen '{file_path}' ble ikke funnet.")
    except Exception as e:
        print(f"En feil oppstod: {e}")

def save_hash_to_file(file_path, hash_value):
    """Lagrer hash-verdien til en fil."""
    hash_file_path = file_path + ".hash"
    try:
        with open(hash_file_path, "w") as hash_file:
            hash_file.write(hash_value)
        print(f"Hash-verdien er lagret til {hash_file_path}")
    except Exception as e:
        print(f"Kunne ikke lagre hash-verdien: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Bruk: python hash_generator.py [filsti]")
    else:
        file_path = sys.argv[1]
        hash_value = generate_hash(file_path)
        if hash_value:
            save_hash_to_file(file_path, hash_value)
