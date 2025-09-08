/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    newArr = [];
    arr.forEach((num, i) => {
        if (fn(arr[i], i)) {
            newArr.push(num);
        }
    });
    return newArr;
};
