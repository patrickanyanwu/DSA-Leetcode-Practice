/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    const curr = init;
    return {
        increment: () => {
            init++;
            return init;
        },
        decrement: () => {
            init--;
            return init;
        },
        reset: () => {
            init = curr;
            return init;
        }
    }
};
