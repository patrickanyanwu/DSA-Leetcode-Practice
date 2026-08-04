"""
I identified invalid transactions by grouping them by name and checking two
conditions: amount exceeds $1000, or same person has transactions in different
cities within 60 minutes. I parse each transaction and group by name, storing
time, amount, city, and original index. For each person's transactions, I sort
by time and check each transaction. If amount > 1000, I mark it invalid. Then
I use a sliding window to find all transactions within 60 minutes and check if
any are in different cities. If so, I mark both as invalid. Finally, I return
the original transaction strings for all marked indices. Sorting by time
enables efficient range checking.
O(n log n) time O(n) space
"""

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        by_name = defaultdict(list)

        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(',')
            by_name[name].append((int(time), int(amount), city, i))

        invalid = [False] * len(transactions)

        for txs in by_name.values():
            txs.sort(key=lambda x: x[0])

            n = len(txs)
            for i in range(n):
                time_i, amount_i, city_i, idx_i = txs[i]

                if amount_i > 1000:
                    invalid[idx_i] = True

                j = i + 1
                while j < n and txs[j][0] - time_i <= 60:
                    time_j, amount_j, city_j, idx_j = txs[j]
                    if city_i != city_j:
                        invalid[idx_i] = True
                        invalid[idx_j] = True
                    j += 1

        return [transactions[i] for i in range(len(transactions)) if invalid[i]]
