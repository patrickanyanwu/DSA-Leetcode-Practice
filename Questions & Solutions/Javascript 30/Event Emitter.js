/* 
  Used a hashmap with the key being the event-name and the value being an array
  containing the array of callbacks for that event and a hashmap with the key being the callback added
  and the value being its index in the array.
  When a user subscribes the callback is added to the eventnames array and the index is added to the eventnames hashmap.
  When a user wants to unsubscribe a callback we swap it with the last element in the array and then pop from the array,
  this allows to keep this an O(1) operation.
  The indexes are updated correctly in the hashmap also.
  O(1) subscribe, unsubscribe and emit is O(n * runtime of callbacks).
*/


class EventEmitter {
    constructor() {
        this.events = new Map();
    }

    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        if (!this.events.has(eventName)) {
            this.events.set(eventName, [[], new Map()]);
        }

        const [callbacks, callbackMap] = this.events.get(eventName);
        callbacks.push(callback);
        callbackMap.set(callback, callbacks.length - 1);

        return {
            unsubscribe: () => {
                const index = callbackMap.get(callback);
                const lastIndex = callbacks.length - 1;

                if (index !== lastIndex) {
                    const lastCallback = callbacks[lastIndex];
                    callbacks[index] = lastCallback;
                    callbackMap.set(lastCallback, index);
                }

                callbacks.pop();
                callbackMap.delete(callback);
            }
        };
    }

    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        if (!this.events.has(eventName)) return [];

        const [callbacks] = this.events.get(eventName);
        return callbacks.map(cb => cb(...args));
    }
}
