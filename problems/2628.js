/**
 * @param {null|boolean|number|string|Array|Object} o1
 * @param {null|boolean|number|string|Array|Object} o2
 * @return {boolean}
 */
 var areDeeplyEqual = function(o1, o2) {
  if (typeof o1 !== typeof o2) return false;
  if (Array.isArray(o1) !== Array.isArray(o2)) return false;

  if (Array.isArray(o1)) {
      if (o1.length !== o2.length) return false;

      for (let i = 0; i < o1.length; i++) {
          if (!areDeeplyEqual(o1[i], o2[i])) return false;
      }
  } else if (o1 && o2 && typeof o1 === 'object' && typeof o2 === 'object'){
      if (Object.keys(o1).length !== Object.keys(o2).length) return false;

      for (const key in o1) {
          // Si la llave del obj1 no está en el obj2 return false
          if (!(key in o2) || !areDeeplyEqual(o1[key], o2[key])) return false;
      }
  } else {
      return o1 === o2;
  }

  return true;
};