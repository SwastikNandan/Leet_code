def isBipartite(self, graph):
    seen = {}
    for node in range(len(graph)):
        if node not in seen:
            seen[node] = 0
            stack = [node]

            while stack:
                cur = stack.pop()

                for nei in graph[cur]:
                    if nei not in seen:
                        stack.append(nei)
                        seen[nei] = seen[cur] ^ 1
                    elif seen[nei] == seen[cur]:
                        return False
    return True