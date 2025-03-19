/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let new1 = new Array(arr.length);
    arr.forEach((num, i) => {
        new1[i] = fn(arr[i], i);
    });
    return new1;
};
