"""
  Using a monotonically increasing stack which holds (price, span of days where previous prices were <= price),
  As we add a new price when next is called we calculate its span by popping from the stack while we have a price <= price,
  we then append the new price and calculated span to the stack and return the span.
  O(1) time O(1) space
"""


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span
        self.stack.append((price, span))
        return span




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
