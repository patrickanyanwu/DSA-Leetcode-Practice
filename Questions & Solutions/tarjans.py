from collections import defaultdict

def tarjans(n, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)

    ids = [-1] * n
    lows = [0] * n
    onStack = [False] * n
    id = [0]
    stack = []
    sccs = []

    def dfs(node):
        ids[node] = lows[node] = id[0]
        id[0] += 1
        stack.append(node)
        onStack[node] = True

        for v in adj[node]:
            if ids[v] == -1:
                dfs(v)
            if onStack[v]:
                lows[node] = min(lows[node], lows[v])

        if ids[node] == lows[node]:
            component = []
            while True:
                curr = stack.pop()
                onStack[curr] = False
                component.append(curr)
                if node == curr:
                    break
            sccs.append(component)

    for i in range(n):
        if ids[i] == -1:
            dfs(i)
    return sccs


def tarjans_iterative(n, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)

    ids = [-1] * n
    lows = [0] * n
    onStack = [False] * n
    stack = []
    sccs = []
    id = [0]

    for start in range(n):
        if ids[start] != -1:
            continue

        ids[start] = lows[start] = id[0]
        id[0] += 1
        stack.append(start)
        onStack[start] = True

        call_stack = [[start, 0]]

        while call_stack:
            node, i = call_stack[-1]

            if i < len(adj[node]):
                call_stack[-1][1] += 1
                v = adj[node][i]

                if ids[v] == -1:
                    ids[v] = lows[v] = id[0]
                    id[0] += 1
                    stack.append(v)
                    onStack[v] = True
                    call_stack.append([v, 0])
                elif onStack[v]:
                    lows[node] = min(lows[node], lows[v])
            else:
                call_stack.pop()

                if ids[node] == lows[node]:
                    component = []
                    while True:
                        curr = stack.pop()
                        onStack[curr] = False
                        component.append(curr)
                        if curr == node:
                            break
                    sccs.append(component)

                if call_stack:
                    parent = call_stack[-1][0]
                    if onStack[node]:
                        lows[parent] = min(lows[parent], lows[node])

    return sccs


if __name__ == "__main__":
    print(tarjans(2, [[0, 1], [1, 0]]))
    print(tarjans(4, [[0, 1], [1, 2], [2, 0], [0, 3]]))
    print(tarjans(3, []))
    print(tarjans(6, [[0, 1], [1, 0], [2, 3], [3, 4], [4, 2], [5, 5]]))
    print(tarjans(4, [[0, 1], [1, 2], [2, 3]]))
    print(tarjans(5, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 3]]))

    print(tarjans_iterative(2, [[0, 1], [1, 0]]))
    print(tarjans_iterative(4, [[0, 1], [1, 2], [2, 0], [0, 3]]))
    print(tarjans_iterative(3, []))
    print(tarjans_iterative(6, [[0, 1], [1, 0], [2, 3], [3, 4], [4, 2], [5, 5]]))
    print(tarjans_iterative(4, [[0, 1], [1, 2], [2, 3]]))
    print(tarjans_iterative(5, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 3]]))
