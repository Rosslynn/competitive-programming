/**
 * @param {Function[]} functions - Peticiones asíncronas que debo ejecutar
 * @param {number} n - Número máximo de peticiones que puedo ejecutar en paralelo
 * @return {Promise<any>}
 */
 var promisePool = function(functions, n) {
  // El número total de promesas que debo ejecutar
  const promisesLength = functions.length;
  // El índice de la promesa que se va a ejecutar
  let currentPromiseIndex = 0
  // La cantidad de promesas que se han resuelto
  let promisesResolved = 0
  // Donde hago un seguimiento de las promesas que se están ejecutando
  const promises = {}

  // Creamos una promesa que se resuelve una vez todas las peticiones al servidor se hayan terminado de ejecutar
  return new Promise((resolve, reject) => {
      if (!promisesLength) {
          resolve('');
          return;
      }
      // Aquí es donde nos aseguramos de ejecutar como máximo el número que recibamos en el umbral
      function executePromise() {
          // Entonces... mientras que el indice de la promesa que se ejecutará sea menor -
          // a la cantidad de promesas que debo ejecutar y tengo ejecuciones disponibles
          while (currentPromiseIndex < promisesLength && Object.keys(promises) < n) {
              // 1. Ejecuta la promesa que está en el indice actual
              promises[currentPromiseIndex] = functions[currentPromiseIndex]()
              .then(() => {
                  // 3. Una vez la promesa se resuelva, añadele 1 al contador
                  promisesResolved += 1;
                  delete promises[currentPromiseIndex];

                  // 4. Si ya se ejecutaron exitosamente todas las promesas simplemente avisa que ya
                  if (promisesResolved == promisesLength) {
                      resolve('');
                      return;
                  }

                  // 5. Si me quedan promesas por ejecutar añadelas al stack
                  if (currentPromiseIndex < promisesLength) {
                      executePromise();
                  }
              }).catch(() => {
                  reject('No pude ejecutar algo D:')
              });
              
              // 2. Avanza a la siguiente promesa
              currentPromiseIndex += 1;
          }
      };

      executePromise();
  });
};

/**
* const sleep = (t) => new Promise(res => setTimeout(res, t));
* promisePool([() => sleep(500), () => sleep(400)], 1)
*   .then(console.log) // After 900ms
*/