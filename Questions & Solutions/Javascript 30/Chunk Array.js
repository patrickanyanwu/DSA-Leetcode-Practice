/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let res = [];
    let new1 = [];
    if (arr.length) {
    arr.forEach((item, i) => {
        new1.push(item);
        if (new1.length === size || i === arr.length - 1) {
            res.push(new1.slice());
            new1 = [];
        }
    })
    } else {
        return [];
    }
    return res;
};
