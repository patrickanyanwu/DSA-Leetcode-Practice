/* 
  Have a hashmap with key being the number and value being its frequency.
  Now as we loop through the array we count frequencies of numbers,
  If k - num is in our map already (we have a valid pair) we decrement the frequency of that k - num as we cant use it again and we dont increment the frequency of the current number either.
  O(n) time O(n) space.
*/

function maxOperations(nums: number[], k: number): number {
    let map = new Map<number, number>();
    let count: number = 0;
    
    for (let i: number = 0; i < nums.length; i++) {
        let num: number = nums[i];
        if (map.has(k - num)) {
            if (map.get(k - num) !== 0) {
                count++;
                map.set(k - num, map.get(k - num) - 1);
                continue;
            } else {
                map.delete(k - num);
            }
        }
        if (map.has(num)) {
            map.set(num, map.get(num) + 1);
        } else {
            map.set(num, 1);
        }
        
    }
    return count;
};
