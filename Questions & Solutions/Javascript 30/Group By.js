/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    map1 = {};
    for (const [i, item] of this.entries()) {
        const res = fn(item);
        const val = map1[res];
        if (val) {
            map1[res].push(item);
        } else {
            map1[res] = [item];
        }
    }
    return map1;
};
