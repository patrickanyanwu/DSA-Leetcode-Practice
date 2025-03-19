/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
  return async function(...args) {
    const timeLimited = new Promise((resolve, reject) => {
        setTimeout(() => {reject("Time Limit Exceeded")}, t)
    })
    return Promise.race([fn(...args), timeLimited]);
  }
};
