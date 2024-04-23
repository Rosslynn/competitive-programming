/**
 * @param {null|boolean|number|string|Array|Object} obj1
 * @param {null|boolean|number|string|Array|Object} obj2
 * @return {null|boolean|number|string|Array|Object}
 */
 var deepMerge = function(obj1, obj2) {
    if (obj1 === null ||
        obj2 === null ||
        Array.isArray(obj1) !== Array.isArray(obj2) ||
        typeof obj1 !== 'object' ||
        typeof obj2 !== 'object'
        ) {
        return obj2;
    }

    let ret;

    if (Array.isArray(obj1) && Array.isArray(obj2)) {
        const n = Math.min(obj1.length, obj2.length);
        ret = new Array(Math.max(obj1.length, obj2.length));

        for (let i = 0; i < n; i++) {
            ret[i] = deepMerge(obj1[i], obj2[i]);
        }

        for (let i = n; i < obj1.length; i++) {
            ret[i] = obj1[i];
        }

        for (let i = n; i < obj2.length; i++) {
            ret[i] = obj2[i];
        }
    } else {
        ret = {};

        for (const key in obj2) {
            if (key in obj1) {
                ret[key] = deepMerge(obj1[key], obj2[key]);
                // Estamos liberando espacio en memoria sin utilizar XD
                delete obj2[key];
                delete obj1[key];
            } else {
                ret[key] = obj2[key];
            }
        }

        for (const key in obj1) {
            ret[key] = obj1[key];
        }
    }

    return ret;
};

/**
 * let obj1 = {"a": 1, "c": 3}, obj2 = {"a": 2, "b": 2};
 * deepMerge(obj1, obj2); // {"a": 2, "c": 3, "b": 2}
 */
