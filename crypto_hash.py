import hashlib
import json

def crypto_hash(data):
    """"
    Return a sha-256 hash of the given data.
    """
    stringfied_data = json.dumps(data)
    return hashlib.sha256(stringfied_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash([2]): {crypto_hash([2])}")

if __name__ == "__main__":
    main();