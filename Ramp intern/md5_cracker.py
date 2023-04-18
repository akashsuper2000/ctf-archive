import hashlib
import itertools

# Fixed salt and MD5 hash
fixed_salt = "c85478896c41"
fixed_hash = "0ed82182bed82835d4ef44843a7dd47f"

# Generate MD5 hash for each 7-letter word using fixed salt
for word in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=7):
    word = ''.join(word)
    salted_word = word + fixed_salt
    md5 = hashlib.md5()
    md5.update(salted_word.encode())
    hash = md5.hexdigest()

    # Compare with fixed hash
    if hash == fixed_hash:
        print(f"Found match! Word is {word}")
        break
