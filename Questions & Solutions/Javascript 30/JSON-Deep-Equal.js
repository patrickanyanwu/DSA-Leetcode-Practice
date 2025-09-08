/*
  First check if their data types arent the same, next check if they are primitive data tipes we can just use the === operator.
  Next for the null case we check if one or the other is numm we use the === operator on them.
  Now for arrays we check if the length of the arrays are equal then for eaxch index in the array we deepequal them recursively.
  Now if one or the other is an array and not both we return false;
  Now for objects we check if the length of their keys array is equal, we then check if the one object has the same keys as the other.
  If they do we deepequal their values.
*/

/**
 * @param {null|boolean|number|string|Array|Object} o1
 * @param {null|boolean|number|string|Array|Object} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    if (typeof o1 !== typeof o2) return false;
    if (typeof o1 !== "object" && typeof o2 !== "object") {
        return o1 === o2;
    }
    if (o1 === null || o2 === null) {
        return o1 === o2;
    }

    if (Array.isArray(o1) && Array.isArray(o2)) {
        if (o1.length !== o2.length) {
            return false;
        }
        let res = true;
        for (let i = 0; i < o1.length; i++) {
            if (res) {
                res = areDeeplyEqual(o1[i], o2[i]);
            }
        }
        return res;
    }

    if (Array.isArray(o1) || Array.isArray(o2)) {
        return false;
    }

    if (Object.keys(o1).length === Object.keys(o2).length){
        let result = true;
        for (key of Object.keys(o1)) {
            if (o2.hasOwnProperty(key)) {
                if (result) {
                    result = areDeeplyEqual(o1[key], o2[key]);
                }
            } else {
                return false;
            }
        }
        return result;
    } else {
        return false;
    }
};
