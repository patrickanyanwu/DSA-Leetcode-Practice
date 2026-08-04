"""
  I solved this in  java as java handles integers in a fixed width wereas python does not.
  a is set to a xor b to get the sum of the 2 numbers withouit the carries,
  b is then set to a and b left shifted by one (this gets us our carry bits)
  We keep going while we have no more carry bits.
  O(1) time O(1) space.
  """

class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            var tmp = (a & b) << 1;
            a = a ^ b;
            b = tmp;
        }
        return a;
    }
}
