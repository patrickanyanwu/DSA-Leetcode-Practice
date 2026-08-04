"""
I designed a parking system that tracks available spaces for three car sizes.
I store the counts in an array where index 0 is big, 1 is medium, and 2 is
small. During initialization, I set each slot with the maximum capacity. When
adding a car, I check if there's space available for that car type by looking
at garage[carType - 1] (subtracting 1 since carType is 1-indexed). If space
exists, I decrement the count and return True; otherwise, I return False. This
simple array-based approach efficiently tracks parking availability with O(1)
operations for both initialization and adding cars.
O(1) time O(1) space
"""

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.garage = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.garage[carType - 1]:
            self.garage[carType - 1] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)