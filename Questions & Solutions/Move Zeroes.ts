/*
  Use 2 pointers and if the item at l is a 0 and the item at r is not we swap them inpace and increment the left,
  or if the number at l is not a 0 we increment also so we find our new swap index.
  We increment r afterwards also.
  O(n) time O(1) sapce.
*/
function moveZeroes(nums: number[]): void {
    let [l, r]: [number, number] = [0, 1];
    while (r < nums.length) {
        if ((nums[l] === 0) && (nums[r] !== 0)) {
            [nums[r], nums[l]] = [nums[l], nums[r]];
            l++;
        } else if (nums[l] !== 0) {
            l++;
        }
        r++;
    }
};
