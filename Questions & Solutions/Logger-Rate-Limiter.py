"""
    Used a hashmap to hold each message and its next allowed timestamp,
    now for each message we check if its in the map,
    if not we add it to the map with its timestamp + 10.
    If the message is in the map we check if the current timestamp
    is allowed or not and return the correct boolean.
    O(1) time O(n) space
"""

class Logger:

    def __init__(self):
        self.map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.map:
            self.map[message] = timestamp + 10
        else:
            if timestamp < self.map[message]:
                return False
            else:
                self.map[message] = timestamp + 10
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)