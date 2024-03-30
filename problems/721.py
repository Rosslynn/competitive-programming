class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
        graph = [[] for _ in range(n)]
        emails = {}
        ret = []

        for i in range(n):
            m = len(accounts[i])

            for j in range(1, m):
                curr_email = accounts[i][j]

                if curr_email in emails:
                    graph[emails[curr_email]].append(i)
                    graph[i].append(emails[curr_email])
                
                emails[curr_email] = i
        
        def dfs(node, depth, seen):
            ret = []

            if node in seen:
                return ret

            seen.add(node)
            
            for neigh in graph[node]:
                ret += dfs(neigh, depth + 1, seen)
            
            if depth:
                return ret + accounts[node][1:]

            return accounts[node][:1] + sorted(list(set(accounts[node][1:] + ret)))

        seen = set()

        for i in range(n):
            joined = dfs(i, 0, seen)

            if joined:
                ret.append(joined)
        
        return ret