from string import digits, ascii_letters, punctuation

# Generate all 4-digit combinations using digits
print("4-digit combinations using digits:")
for i in digits:
    for j in digits:
        for k in digits:
            for l in digits:
                print(i, j, k, l)

# Generate all 4-character combinations using letters (both upper and lower case)
print("\n4-character combinations using letters:")
for i in ascii_letters:
    for j in ascii_letters:
        for k in ascii_letters:
            for l in ascii_letters:
                print(i, j, k, l)

# Generate all 4-character combinations using letters, digits, and punctuation
print("\n4-character combinations using letters, digits, and punctuation:")
for i in ascii_letters + digits + punctuation:
    for j in ascii_letters + digits + punctuation:
        for k in ascii_letters + digits + punctuation:
            for l in ascii_letters + digits + punctuation:
                print(i, j, k, l)

# Increase complexity to 8 characters
print("\n8-character combinations using letters, digits, and punctuation:")
for i in ascii_letters + digits + punctuation:
    for j in ascii_letters + digits + punctuation:
        for k in ascii_letters + digits + punctuation:
            for l in ascii_letters + digits + punctuation:
                for m in ascii_letters + digits + punctuation:
                    for n in ascii_letters + digits + punctuation:
                        for o in ascii_letters + digits + punctuation:
                            for p in ascii_letters + digits + punctuation:
                                print(i, j, k, l, m, n, o, p)
