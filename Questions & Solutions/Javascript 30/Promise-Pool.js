/*
  Use a recursive function to call at most n promises.
  The while loop calls n promises at a time and as soon as one is resolved it calls the function again to call more promises.
  Once we have reached the final index of the promises array and we have no current promises running we return.
  O(n) time O(n) space.
*/
/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Promise<any>}
 */
var promisePool = async function(functions, n) {
    return new Promise((resolve) => {
        let inProgressCount = 0;
        let functionIndex = 0;
        function helper() {
            if (functionIndex >= functions.length) {
                if (inProgressCount === 0) resolve();
                return;
            }

            while (inProgressCount < n && functionIndex < functions.length) {
                inProgressCount++;
                const promise = functions[functionIndex]();
                functionIndex++;
                promise.then(() => {
                    inProgressCount--;
                    helper();
                });
            }
        }
        helper();
    });
};
