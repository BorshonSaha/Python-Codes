letters = ["a", "b", "c"]

# Add
letters.append("d")
letters.insert(0, "x")
print(letters)

# Remove
letters.pop()
letters.pop(0)
print(letters)

letters.remove("b")
print(letters)


alphabets = ["a", "b", "c", "d", "e", "f", "g"]
del alphabets[0:3]
print(alphabets)
alphabets.clear()
print(alphabets)
