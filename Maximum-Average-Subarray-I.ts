/*
  Use fixed length sliding window and keep track of the max average using a max variable.
  Slide the window along and decrement and increment our current sum accordingly.
  O(n) time O(1) space.
*/

function findMaxAverage(nums: number[], k: number): number {
    let max: number = Number.MIN_SAFE_INTEGER;
    let [l, r]: [number, number] = [0, 0];
    let cur: number = 0;
    while (r < k) {
        cur += nums[r];
        r++;
    }

    max = Math.max(max, cur / k);
    while (r < nums.length) {
        cur += nums[r];
        cur -= nums[l];
        l++;             

        max = Math.max(max, cur / k);
        r++;  
    }

    return max;
}
