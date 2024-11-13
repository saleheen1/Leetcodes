from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        stk = [node]
        old_to_new = {}
        visited = set()
        visited.add(node)

        while stk:
            popped = stk.pop()
            old_to_new[popped] = Node(val=popped.val)

            for neighbour in popped.neighbors:
                if neighbour not in visited:
                    stk.append(neighbour)
                    visited.add(neighbour)
        
        for key, value in old_to_new.items():
            for oldNeighbour in key.neighbors:
                newNeighbour = old_to_new[oldNeighbour]
                value.neighbors.append(newNeighbour)
        
        return old_to_new[node]


