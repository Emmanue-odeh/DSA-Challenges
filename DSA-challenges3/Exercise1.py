def two_sum(numbers, target):
    seen = {}

    for i, num in enumerate(numbers):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i

    return None


print(two_sum([2, 7, 11, 15], 9))