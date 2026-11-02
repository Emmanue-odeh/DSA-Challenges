def valid_parentheses(text):
    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in text:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0


print(valid_parentheses("{[()]}"))  # True
print(valid_parentheses("([)]"))    # False
print(valid_parentheses("((()))"))  # True
print(valid_parentheses("{[}"))     # False