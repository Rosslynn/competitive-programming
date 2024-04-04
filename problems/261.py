from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Create an undirected graph to check if there is a cycle
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # store the seen nodes and the parents of the children
        seen = {0}
        parents = { 0: None }
        # Si el neighbor ya ha sido visto significa que el node debe si o si ser el hijo de neighbor
        # porque el arbol va de arriba hacia abajo, si esto no se cumple es porque hay un ciclo
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    parents[neighbor] = node

                    if not dfs(neighbor):
                        return False

                elif parents[node] != neighbor:
                    return False

            return True

        # This will return False if a cycle exist else True
        # it does not matter where we start because we the graph is undirected 
        # What matters is that the graph is acyclic and that the length of the seen is equal to N
        is_valid_graph = dfs(0)

        if not is_valid_graph:
            return False

        # At the end we only need to check if the length of the nodes seen are equal to n
        # If they are not the given graph has more than 1 component
        return len(seen) == n

            
'''
no ciclo
https://assets.leetcode.com/uploads/2021/03/12/tree1-graph.jpg
n = 5,
[[0,1],[1,2],[2,3],[1,3],[1,4]]


ciclo:
https://assets.leetcode.com/uploads/2021/03/12/tree2-graph.jpg
n = 5,
[[0,1],[1,2],[2,3],[1,3],[1,4]]
'''