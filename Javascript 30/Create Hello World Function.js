var createHelloWorld = function() {
    let hi = "Hello World";
    return function(...args) {
        return hi;
    }
};
