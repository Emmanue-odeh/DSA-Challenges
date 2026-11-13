def find_number(numbers, target):

    for i, number in enumerate(numbers):
        if number == target:
            return i
    return -1
print(find_number([10, 25, 30, 45], 45)) 