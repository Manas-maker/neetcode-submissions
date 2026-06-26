"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        def bfc(oldNode):
            seen = {}
            cur = oldNode
            newcur = newRoot = Node()
            newcur.val = cur.val
            seen[cur]=newcur
            q = collections.deque()
            q.append((cur, newcur))
            while q:
                cur, newcur = q.popleft()
                if not cur.neighbors: continue
                for neighbor in cur.neighbors:
                    if neighbor not in seen:
                        newNeighbor = Node()
                        newNeighbor.val = neighbor.val
                        q.append((neighbor, newNeighbor))
                        seen[neighbor] = newNeighbor
                    else: newNeighbor = seen[neighbor]
                    newcur.neighbors.append(newNeighbor)
            return newRoot
        return bfc(node)