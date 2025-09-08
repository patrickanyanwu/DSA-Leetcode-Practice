/*
  Using 2 pointers, one at word 1 and second at word 2.
  We then append each letter to a result variable alternatelt.
  If one pointer goes out of bounds we fill up the result with the remaining letters from the other word.
  O(N + M) time O(N + M) space.
*/

function mergeAlternately(word1: string, word2: string): string {
    let res: string = "";
    let [l, r]: [number, number] = [0, 0];
    while ((l < word1.length) && (r < word2.length)) {
        res += word1[l];
        l++;
        res += word2[r];
        r++
    }

    while (l < word1.length) {
        res += word1[l];
        l++;
    }
    while (r < word2.length) {
        res += word2[r];
        r++;
    }
    return res;
};
