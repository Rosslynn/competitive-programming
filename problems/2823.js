/**
 * @param {Object|Array} obj
 * @param {Function} fn
 * @return {Object|Array|undefined}
 */
 var deepFilter = function(obj, fn) {
  if (obj === null || typeof obj !== 'object') {
      return fn(obj) ? obj : undefined;
  }

  let newObj, ret;

  if (Array.isArray(obj)) {
      newObj = [];

      for (let i = 0; i < obj.length; i++) {
          ret = deepFilter(obj[i], fn);

          if (ret !== undefined) {
              newObj.push(ret);
          }
      }

      return newObj.length ? newObj : undefined;
  } 

  newObj = {};

  for (const key in obj) {
      ret = deepFilter(obj[key], fn);

      if (ret !== undefined) {
          newObj[key] = ret;
      }
  }

  return Object.keys(newObj).length ? newObj : undefined;
};