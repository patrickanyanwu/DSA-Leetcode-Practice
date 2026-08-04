"""
I used BFS to find the shortest mutation
path from start to end gene. For each gene,
I tried all possible single-character
mutations (8 positions × 4 genes = 32
possibilities), checking if the mutation
exists in the bank and hasn't been visited.
BFS guarantees finding the minimum number of
mutations needed.
O(n * m * k) time O(n) space
"""

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1
        
        q = deque([(startGene, 0)])
        visited = set([startGene])
        genes = ['A', 'C', 'G', 'T']

        while q:
            gene, steps = q.popleft()
            if gene == endGene:
                return steps

            for i in range(len(gene)):
                for g in genes:
                    if g == gene[i]:
                        continue
                    mutated = gene[:i] + g + gene[i+1:]
                    if mutated in bank and mutated not in visited:
                        visited.add(mutated)
                        q.append((mutated, steps + 1))

        return -1