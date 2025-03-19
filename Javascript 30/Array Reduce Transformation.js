/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let val = init;
    if (!nums.length) {
        return init;
    }
    nums.forEach((num, i) => {
        val = fn(val, num);
    });
    return val;
};
