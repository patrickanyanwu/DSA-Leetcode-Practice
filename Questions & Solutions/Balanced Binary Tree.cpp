/*
I used a bottom-up approach to check if the
tree is balanced. I computed the height of
each subtree and returned -1 if unbalanced,
allowing early termination when an imbalance
is detected.
O(n) time O(h) space
*/

class Solution {
    int height(TreeNode* node) {
        if (!node) return 0;
        int lh = height(node->left);
        if (lh == -1) return -1;     
        int rh = height(node->right);
        if (rh == -1) return -1;        
        if (abs(lh - rh) > 1) return -1;   
        return 1 + max(lh, rh);            
    }
public:
    bool isBalanced(TreeNode* root) {
        return height(root) != -1;
    }
};