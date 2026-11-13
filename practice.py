#def find_largest(numbers):
    #if not numbers:
     #   return None

    #largest = numbers[0]

    #for num in numbers:
    #    if num > largest:
   #         largest = num

  #  return largest
# print(find_largest([3, 41, 56, 78, 7]))


# def list_sum(numbers):
  #  total = 0

   # for num in numbers:
    #    total += num
    #return total
# print(list_sum([2, 4, 6, 8]))


#def count_even(numbers):
 #   count = 0

  #  for num in numbers:
   #     if num % 2 == 0:
    #        count += 1
    #return count
#print(count_even([1, 2, 3, 4, 6]))

#  def count_occurrences(numbers, target):
   #   count = 0

    #  for num in numbers:
       #   if num == target:
          #    count += 1
 #     return count

#  print(count_occurrences([2, 5, 2, 8, 2], 2))

#def find_number(numbers, target):

 #   for i, number in enumerate(numbers):
  #      if number == target:
   #         return i
    #return -1

#print(find_number([10, 20, 40, 38], 20))

#def reverse_list(items):
 #   result = []

  #  for i in range(len(items) -1, -1, -1):
   #     result.append(items[i])

    #return result
# print(reverse_list([1, 2, 3, 4]))

# def has_duplicates(numbers):

  #   return len(numbers) != len(set(numbers))

# print(has_duplicates([1, 2, 3, 2]))