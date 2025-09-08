/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        let promiseCount = 0;
        let res = new Array(functions.length);

        for (const [i, func] of functions.entries()) {
            func() 
            .then(val => {
                res[i] = val;
                promiseCount++;
                if (promiseCount === functions.length) {
                    resolve(res);
                }
            })
            .catch(err => {reject(err)})
        }
    })
};
