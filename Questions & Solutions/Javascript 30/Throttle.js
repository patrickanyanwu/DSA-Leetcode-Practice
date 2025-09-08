/* 
  have 2 variables, one to hold if a function is active and the second to hold pending arguments.
  Now the throttle function check if we have no active function call we set active to true and we set a timeout.
  Whenever the function is called later if the original call is still active we store the arguments.
  After the timeout finishes if there are stored arguments we set active to false and reursively call throttle to run the process again and we clear our saved arguments.
*/

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let active = false;
    let arg1 = "no";
    throttled = function(...args) {
        if (!active) {
            active = true;
            setTimeout(() => {
                active = false;
                if (arg1 !== "no") {
                    throttled(...arg1);
                    arg1 = "no";
                }
            }, t)
            return fn(...args);
        } else {
            arg1 = args;
        }
    }
    return throttled
};
