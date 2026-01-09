"""
I designed an underground system that tracks check-ins and calculates average
journey times. I use two dictionaries: checkins maps passenger IDs to their
check-in station and time, while journeys maps (start, end) station pairs to
a list containing total time and trip count. When checking in, I store the
passenger's station and time. When checking out, I retrieve their check-in
info, calculate the duration, and update the journey totals for that route.
For getting average time, I simply divide the total time by the count for
that route. This design efficiently tracks all journeys with constant time
operations.
O(1) time per operation, O(P + S²) space where P is passengers, S is stations
"""

class UndergroundSystem:

    def __init__(self):
        self.checkins = {}   # id -> (station, time)
        self.journeys = {}   # (start, end) -> [total_time, count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, start_time = self.checkins.pop(id)
        duration = t - start_time
        key = (start, stationName)

        if key in self.journeys:
            self.journeys[key][0] += duration
            self.journeys[key][1] += 1
        else:
            self.journeys[key] = [duration, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.journeys[(startStation, endStation)]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)