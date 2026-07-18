import time

nodes = {
    (0, 0),
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 0),
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 0),
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4),
    (2, 5),
    (3, 0),
    (3, 1),
    (3, 2),
    (3, 3),
    (3, 4),
    (3, 5),
    (4, 0),
    (4, 1),
    (4, 2),
    (4, 3),
    (4, 4),
    (4, 5),
    (5, 0),
    (5, 1),
    (5, 2),
    (5, 3),
    (5, 4),
    (5, 5),
    (6, 0),
    (6, 1),
    (6, 2),
    (6, 3),
    (6, 4),
    (6, 5),
    (7, 1),
    (7, 2),
    (7, 3),
    (7, 4),
    (7, 5),
    (8, 4),
    (8, 5),
    (8, 6),
}


def create_graph(nodes):
    graph = {}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for row, col in nodes:
        graph[(row, col)] = []
        for row_change, col_change in directions:
            neighbor = (row + row_change, col + col_change)
            if neighbor in nodes:
                graph[(row, col)].append(neighbor)

    return graph


def creates_dead_end(graph, visited, moved_node, destination):
    """After marking `moved_node` visited, check whether any of ITS
    neighbors just became stranded: an unvisited, non-destination node
    with zero remaining unvisited neighbors can never be entered or
    exited again, so the branch is unsalvageable."""
    for neighbor in graph[moved_node]:
        if neighbor in visited or neighbor == destination:
            continue
        remaining = 0
        for n2 in graph[neighbor]:
            if n2 not in visited:
                remaining += 1
        if remaining == 0:
            return True
    return False


def remaining_connected(graph, current, destination, visited, total_nodes):
    """Verify that the destination AND every other unvisited node are
    still reachable from `current`, moving only through unvisited nodes
    (destination may be passed through as a terminal target). If any
    unvisited node is cut off into an unreachable pocket, this branch
    can never complete a Hamiltonian path, so we prune it."""
    unvisited_count = total_nodes - len(visited)

    if current == destination:
        return unvisited_count == 0

    stack = [current]
    seen = {current}
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor in seen:
                continue
            if neighbor == destination or neighbor not in visited:
                seen.add(neighbor)
                stack.append(neighbor)

    if destination not in seen:
        return False

    reached_unvisited = sum(1 for n in seen if n not in visited)
    return reached_unvisited == unvisited_count


def find_all_nodes_path(graph, start, destination):
    path = [start]
    visited = {start}
    total_nodes = len(graph)
    call_count = [0]

    def backtrack(current):
        call_count[0] += 1
        if call_count[0] % 200000 == 0:
            print(
                f"Calls: {call_count[0]:,}  path length: {len(path)}  current: {current}"
            )

        if len(path) == total_nodes:
            return current == destination

        if current == destination:
            return False

        candidates = []
        for neighbor in graph[current]:
            if neighbor in visited:
                continue
            # Only allow stepping into destination if it is the LAST
            # remaining unvisited node.
            if neighbor == destination and len(visited) != total_nodes - 1:
                continue
            candidates.append(neighbor)

        # Most-constrained-first heuristic (Warnsdorff-style).
        candidates.sort(key=lambda node: sum(n not in visited for n in graph[node]))

        for neighbor in candidates:
            visited.add(neighbor)
            path.append(neighbor)

            if not creates_dead_end(
                graph, visited, neighbor, destination
            ) and remaining_connected(
                graph, neighbor, destination, visited, total_nodes
            ):
                if backtrack(neighbor):
                    return True

            path.pop()
            visited.remove(neighbor)

        return False

    if backtrack(start):
        return path.copy()

    return None


graph = create_graph(nodes)
start = (2, 2)
destination = (8, 6)

t0 = time.perf_counter()
path = find_all_nodes_path(graph, start, destination)
t1 = time.perf_counter()

if path is None:
    print("No path was found.")
else:
    print("Number of visited nodes:", len(path))
    print("Path:")
    for node in path:
        print(node)

print(f"Elapsed: {t1 - t0:.4f} seconds")
