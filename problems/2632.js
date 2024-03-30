/**
 * @param {Function} fn
 * @return {Function}
 */
 var curry = function(fn) {
  const currParams = [];
  
  return function curried(...args) {
      currParams.push(...args);

      if (currParams.length === fn.length) {
          return fn(...currParams);
      }

      return curried;
  }
};

/**
* function sum(a, b) { return a + b; }
* const csum = curry(sum);
* csum(1)(2) // 3
*/
