/**
 * @return {Object}
 */
 var createInfiniteObject = function() {
  const validator = {
      get(obj, prop, receiver) {
          return function() {
              return prop;
          };
      },
  };

  const obj = {
      user: {
          age: 15,
          meta: {
              location: 'bogota',
          }
      },
  };

  return new Proxy(obj, validator);
};

/**
* const obj = createInfiniteObject();
* obj['abc123'](); // "abc123"
*/