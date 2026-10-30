def path_exists(graph, start, target):
    visited = set()
    stack = [start]

    while stack:
        current = stack.pop()

        if current == target:
            return True

        if current not in visited:
            visited.add(current)

            for neighbour in graph[current]:
                stack.append(neighbour)

    return False


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": ["F"],
    "F": []
}

print(path_exists(graph, "A", "F"))
print(path_exists(graph, "D", "A"))