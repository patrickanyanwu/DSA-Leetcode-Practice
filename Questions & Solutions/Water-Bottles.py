"""
I simulated the process of drinking bottles and exchanging empty ones for new bottles. 
I kept track of the total bottles drunk and repeatedly exchanged empty bottles while possible, 
adding the leftover bottles to the next round until I couldn't exchange anymore.
O(log n) time O(1) space
"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            new_bottles = numBottles // numExchange
            res += new_bottles
            numBottles = new_bottles + numBottles % numExchange
        return res