class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        from collections import defaultdict
        
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = set()
        complete_count = 0
        
        def dfs(node, component):
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    component.add(curr)
                    stack.extend(graph[curr] - visited)

        for i in range(n):
            if i not in visited:
                component = set()
                dfs(i, component)
                
                k = len(component)
                expected_edges = k * (k - 1) // 2
                actual_edges = sum(len(graph[v]) for v in component) // 2
                if actual_edges == expected_edges:
                    complete_count += 1

        return complete_count
