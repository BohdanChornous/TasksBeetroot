import sys

# Task 2


def dijsktra(graph: dict, src: str, dest: str) -> None:
    inf = sys.maxsize
    way = [dest]
    visited_nodes = []
    unvisited_nodes = [node for node in graph.keys()]
    cost_of_visiting = {}
    for node in graph.keys():
        if node == src:
            cost_of_visiting[node] = {"cost": 0, 'prev': None}
        else:
            cost_of_visiting[node] = {"cost": inf, 'prev': None}
    temp = src
    while unvisited_nodes:
        current_vis = []
        for visitors, cost in graph[temp].items():
            if visitors in visited_nodes:
                continue
            if cost_of_visiting[visitors]['prev'] is None and cost_of_visiting[visitors]['cost'] == inf:
                cost_of_visiting[visitors]['prev'] = temp
                cost_of_visiting[visitors]["cost"] = cost_of_visiting[temp]['cost'] + cost
            if cost_of_visiting[temp]['cost'] + cost < cost_of_visiting[visitors]['cost']:
                cost_of_visiting[visitors]['cost'] = cost_of_visiting[temp]['cost'] + cost
                cost_of_visiting[visitors]['prev'] = temp
            current_vis.append((visitors, cost_of_visiting[visitors]['cost']))
        visited_nodes.append(unvisited_nodes.pop(unvisited_nodes.index(temp)))
        if unvisited_nodes:
            if current_vis:
                temp = min(current_vis, key=lambda x: x[1])[0]
            else:
                temp = unvisited_nodes[0]
    current = dest
    while current != src:
        way += [cost_of_visiting[current]['prev']]
        current = cost_of_visiting[current]['prev']
    print("This is the way: " + "->".join(way[::-1]))
    print(f"Shortest Distance: {cost_of_visiting[dest]['cost']}")


if __name__ == "__main__":
    my_graph = {
        'A': {'B': 2, 'D': 8},
        'B': {'A': 2, 'E': 6, 'D': 5},
        'C': {'E': 9, 'F': 3},
        'D': {'A': 8, 'B': 5, 'E': 3, 'F': 2},
        'E': {'B': 6, 'D': 3, 'F': 1, 'C': 9},
        'F': {'D': 2, 'E': 1, 'C': 3}
    }

    source = 'F'
    destination = 'C'
    dijsktra(my_graph, source, destination)
