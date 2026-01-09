"""
I designed a browser history system using a doubly linked list. Each node
represents a URL with prev and next pointers. I track the current page with a
pointer. When visiting a new URL, I create a node, link it to current, and
move current forward, effectively clearing any forward history. For back(), I
move the current pointer backward up to the specified steps (or until reaching
the oldest page), returning the final URL. For forward(), I move current
forward up to the specified steps (or until reaching the newest page). The
doubly linked list naturally maintains the history chain and allows efficient
bidirectional navigation.
O(1) time for visit, O(min(steps, history_size)) for back/forward, O(n) space
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = new_node

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.val