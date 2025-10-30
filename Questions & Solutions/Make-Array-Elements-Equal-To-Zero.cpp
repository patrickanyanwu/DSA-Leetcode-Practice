/*
    I simulated movement from each zero index in
    both directions. For each zero, I tried left
    and right, flipping direction when hitting
    nonzero elements and decrementing them. I
    counted valid starting positions.
    O(n^2 * m) time O(n) space
*/

class Solution {
public:
    int countValidSelections(vector<int>& nums) {
        int n = nums.size();
        vector<int> zeros;
        int res = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) zeros.push_back(i);
        }

        for (int idx : zeros) {
            if (simulate(nums, idx, true)) res++;
            if (simulate(nums, idx, false)) res++;
        }

        return res;
    }

private:
    bool simulate(const vector<int>& original, int curr, bool moveLeft) {
        vector<int> nums = original;
        int n = nums.size();

        while (curr >= 0 && curr < n) {
            if (nums[curr] == 0) {
                curr += moveLeft ? -1 : 1;
            } else {
                nums[curr]--;
                moveLeft = !moveLeft;
                curr += moveLeft ? -1 : 1;
            }
        }

        for (int x : nums) {
            if (x != 0) return false;
        }
        return true;
    }
};