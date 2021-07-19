# https://leetcode.com/problems/accounts-merge/

class Solution:
    
    def _dfs(self, graph, u, visited, merged_account):
        for account in graph[u]:
            n = len(account)
            for i in range(1, n):
                if account[i] not in visited:
                    visited.add(account[i])
                    merged_account.append(account)
                    self._dfs(graph, account[i], visited, merged_account)
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}
        for account in accounts:
            n = len(account)
            for i in range(1, n):
                try:
                    graph[account[i]].append(account)
                except:
                    graph[account[i]] = [account]
        #print(graph)
        visited = set()
        res = []
        for email in graph.keys():
            #print(email)
            if email not in visited:
                merged_account = []
                self._dfs(graph, email, visited, merged_account)
                res.append(merged_account)
        
        for i in range(len(res)):
            accounts = res[i]
            formated_account = [accounts[0][0]]
            emails_set = set()
            for account in accounts:
                n = len(account)
                for j in range(1, n):
                    emails_set.add(account[j])
            
            formated_account.extend(sorted(emails_set))
            res[i] = formated_account
        return res
