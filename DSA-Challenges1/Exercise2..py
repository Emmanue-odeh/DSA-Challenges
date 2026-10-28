def find_smallest(numbers):
    if not numbers:
        return None

    largest = numbers[0]

    for number in numbers:
      if number < largest:
         largest = number

    return largest

print(find_smallest([8, 3, 12, 1, 7]))