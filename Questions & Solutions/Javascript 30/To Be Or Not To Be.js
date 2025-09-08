/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: function(value){
            if (value === val) {
                return true;
            }
            throw new Error("Not Equal");
        },
        notToBe: function(value){
            if (value !== val) {
                return true;
            }
            throw new Error("Equal");
        }
    }
};
