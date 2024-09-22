import itertools

# Known part of the flag
known_prefix = "acdfCTF{"
known_suffix = "}"

# Brute force possible inner values
charset = "abcdefghijklmnopqrstuvwxyz0123456789"  # Adjust based on possibilities
for combo in itertools.product(charset, repeat=5):  # Adjust length based on the expected size
    possible_flag = known_prefix + ''.join(combo) + known_suffix
    print("Trying:", possible_flag)
    # Here, insert logic to test the flag in the target application
