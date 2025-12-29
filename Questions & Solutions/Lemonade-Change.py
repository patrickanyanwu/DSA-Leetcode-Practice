"""
I simulated the lemonade stand transaction process by tracking $5 and $10
bills as change. For each customer, if they pay $5, I keep it. If they pay
$10, I need to give back $5 change. If they pay $20, I prefer giving one $10
and one $5 (if available) since $5 bills are more versatile, otherwise I give
three $5 bills. If I can't provide correct change at any point, I return
False. By greedily using $10 bills when giving change for $20, I preserve
more $5 bills for future transactions. This greedy strategy ensures optimal
change management.
O(n) time O(1) space
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True