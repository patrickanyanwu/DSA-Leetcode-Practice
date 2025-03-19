/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    let cancelled = false;
    fn(...args);
    var refreshIntervalId = setInterval(() => {
        if (!cancelled) {
            fn(...args);
        } else {
            clearInterval(refreshIntervalId);
        }
    }, t)
    return () => {
        cancelled = true;
    }
};
