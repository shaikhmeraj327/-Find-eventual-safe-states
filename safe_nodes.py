from collections import deque


def eventual_safe_nodes(vertices, edges):
    reverse_graph = [[] for _ in range(vertices)]
    out_degree = [0] * vertices

    for source, target in edges:
        reverse_graph[target].append(source)
        out_degree[source] += 1

    queue = deque(node for node in range(vertices) if out_degree[node] == 0)
    safe = [False] * vertices

    while queue:
        node = queue.popleft()
        safe[node] = True

        for predecessor in reverse_graph[node]:
            out_degree[predecessor] -= 1
            if out_degree[predecessor] == 0:
                queue.append(predecessor)

    return [node for node, is_safe in enumerate(safe) if is_safe]


def eventualSafeNodes(vertices, edge_count, edges):
    if edge_count < len(edges):
        edges = edges[:edge_count]
    return eventual_safe_nodes(vertices, edges)


class Solution:
    def eventualSafeNodes(self, vertices, edge_count, edges):
        if edge_count < len(edges):
            edges = edges[:edge_count]
        return eventual_safe_nodes(vertices, edges)
