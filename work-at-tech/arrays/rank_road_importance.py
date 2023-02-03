class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Track occurences
        occurences = {i :0 for i in range(0, n)}
        for road in roads:
            occurences[road[0]] += 1
            occurences[road[1]] += 1
        
        # Sort by occurences, rank importance
        occurences = dict(sorted(occurences.items(), key=lambda item: item[1], reverse=False))
        keys = list(occurences.keys())
        importance = {keys[i] :i+1 for i in range(0, n)}
        
        # Add up importances
        retval = 0
        for road in roads:
            retval += importance[road[0]] + importance[road[1]]
        return retval
        