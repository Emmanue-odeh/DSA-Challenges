def first_unique(text):
    counts = {}

    for char in text:
        counts[char] = counts.get(char, 0) + 1

    for char in text:
        if counts[char] == 1:
            return char

    return None


print(first_unique("leetcode"))   # l
print(first_unique("aabbcddee"))  # c
print(first_unique("aabbcc"))     # None