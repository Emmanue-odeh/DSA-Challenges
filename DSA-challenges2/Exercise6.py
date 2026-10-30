def closest_number(numbers, target):
    closest = numbers[0]

    for num in numbers:
        distance = abs(num - target)
        closest_distance = abs(closest - target)

        if distance < closest_distance or (distance == closest_distance and num < closest):
            closest = num

    return closest

print(closest_number([4, 8, 15, 20], 13))
print(closest_number([8, 12], 10))
print(closest_number([1, 5, 9], 2))