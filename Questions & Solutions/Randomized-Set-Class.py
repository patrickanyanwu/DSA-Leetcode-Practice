"""I use and array and a dictionary as arrays are O(1) for getrandom and they also have O(1) pop and O(1) append, i also used a dictionary as they have O(1) add and O(1) remove. 
Dictionary is used for holding the indexes of the numbers in the array so when we want to remove we know the index of the element in the array.
When removing we get the index of the element we want to remove from our hashmap then we check if the element is not already the last element in the array,
if it is we just pop and delete from the hashmap. If not we swap the index of the element we want to remove with the index of the last elemnt in the array,
we then update that index and delete the element we want to delete from the hashmap while we also pop from the array.
O(1) time O(n) space."""

class RandomizedSet:
    def __init__(self):
        self.map = {}
        self.arr = []
    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.arr.append(val)
            self.map[val] = len(self.arr) - 1
            return True
        else:
            return False
     
    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        
        index = self.map[val]
        last_element = self.arr[-1]

        if index != len(self.arr) - 1:
            self.arr[index] = last_element
            self.map[last_element] = index

        self.arr.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
