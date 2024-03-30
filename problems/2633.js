/**
 * @param {null|boolean|number|string|Array|Object} object
 * @return {string}
 */
 var jsonStringify = function(object) {  
  const output = [];

  if (Array.isArray(object)) {
      output.push('[');

      for (let i = 0; i < object.length; i++) {
          if (output.length > 1) output.push(',');
          output.push(jsonStringify(object[i]));
      }

      output.push(']');
  } else if (object !== null && typeof object ==='object') {
      output.push('{');

      for (let key in object) {
          if (output.length > 1) output.push(',')
          output.push(`"${key}":${jsonStringify(object[key])}`)
      }

      output.push('}');
  } else {
      if (typeof object === 'string') output.push(`"${object}"`);
      else if (object === null) output.push('null')
      else output.push(object)
  }

  return output.join('');
};

/*
  Input: object = {"y":1,"x":2}
  Output: {"y":1,"x":2}
  Explanation: 
  Return the JSON representation.
  Note that the order of keys should be the same as the order returned by Object.keys().
*/