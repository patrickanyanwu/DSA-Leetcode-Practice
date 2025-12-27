"""
    I calculated the average salary excluding minimum and maximum by first
    finding the min and max values in the array. Then I iterate through all
    salaries and sum only those that are neither the minimum nor maximum
    using a chained comparison (maxi != s != mini). Finally, I divide the
    sum by n - 2 since I excluded exactly two salaries. The division by n - 2 gives the correct
    average of the remaining salaries.
    O(n) time O(1) space
"""
class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        mini = min(salary)
        maxi = max(salary)

        total_sum = 0

        for s in salary:
            if maxi != s != mini:
                total_sum += s
        
        return total_sum / (n - 2)