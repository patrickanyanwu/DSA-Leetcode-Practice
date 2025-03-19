/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    if (n === 0) return arr;

    let result = [];

    const helper = (subArr, depth) => {
        for (let el of subArr) {
            if (Array.isArray(el) && depth < n) {
                helper(el, depth + 1);
            } else {
                result.push(el);
            }
        }
    };

    helper(arr, 0);
    return result;
};
