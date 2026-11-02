def has_cycle(graph):
    visited = set()
    current_path = set()

    def dfs(node):
        if node in current_path:
            return True

        if node in visited:
            return False

        visited.add(node)
        current_path.add(node)

        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True

        current_path.remove(node)

        return False

    for node in graph:
        if dfs(node):
            return True

    return False


graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}

print(has_cycle(graph))  