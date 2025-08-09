s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

num_vowels = 0
for ch in s:
    for vowel in vowels:
        if ch == vowel:
            num_vowels += 1

print(f"Number of vowel in sentence: {num_vowels}")