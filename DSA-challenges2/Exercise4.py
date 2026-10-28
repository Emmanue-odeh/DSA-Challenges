from collections import deque
def reverse_first(queue, k):
    queue = deque(queue)

    if k < 0 or k > len(queue):
        return list(queue)

    stack = []

    for i in range(k):
        stack.append(queue.popleft())

    while stack:
        queue.appendleft(stack.pop())

    return list(queue)


print(reverse_first([10, 20, 30, 40, 50], 3))
print(reverse_first([1, 2, 3, 4], 2))
