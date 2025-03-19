/* Create a closure which allows returned function to remmeber the variable in outer scope*/

/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let count = n - 1;
    return function() {
        count++;
        return count;
    };
};
