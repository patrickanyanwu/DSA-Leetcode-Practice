/*
    I tracked the left and right sums as I
    traversed the array. At each zero position,
    I checked if the difference between left
    and right sums was 0 or 1, counting valid
    selections in both directions.
    O(n) time O(1) space
*/

class Solution {
public:
    int countValidSelections(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        int sum = accumulate(nums.begin(), nums.end(), 0);
        int leftSum = 0;
        int rightSum = sum;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                if (leftSum - rightSum == 0 || leftSum - rightSum == 1) {
                    ans++;
                }
                if (rightSum - leftSum == 0 || rightSum - leftSum == 1) {
                    ans++;
                }
            } else {
                leftSum += nums[i];
                rightSum -= nums[i];
            }
        }
        return ans;
    }
};