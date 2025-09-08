/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let run;
    return function(...args){
        if (fn) {
            run = fn.apply(this, args);
            fn = null;
            return run;
        }
        return undefined;
    }
};
