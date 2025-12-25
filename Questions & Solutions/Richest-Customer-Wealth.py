class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        I found the richest customer by calculating each customer's total wealth
        and returning the maximum. I use a generator expression that sums each
        customer's bank accounts (each row in the 2D array) and pass it to the
        max function. This one-liner approach iterates through all customers,
        computes their total wealth by summing their account balances, and
        identifies the largest sum. This is concise and efficient, avoiding the
        need for explicit loops or tracking variables.
        O(n × m) time O(1) space
        """
        return max(sum(bank) for bank in accounts)