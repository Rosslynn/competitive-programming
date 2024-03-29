class Solution:
    def countSubarrays(self, nums, k):
        max_num = max(nums)
        n = len(nums)
        ret = freq = left = 0
       
        for i in range(n):
            if nums[i] == max_num:
                freq += 1
            
            while freq == k:
                if nums[left] == max_num:
                    freq -= 1
                
                left += 1
            
            ret += left
        
        return ret

'''
[1,3,2,3,3]

Si nos detenemos en el indice 3 la cantidad de sub arrays validos es 2
  -> [1,3,2,3], [3,2,3]

Movemos left hacia la derecha hasta hacer invalido la ventana, al final left cuenta cuantos sub arrays validos hay
  -> Si nos detenemos en el indice 4 y repetimos y empezamos desde 0 a encoger la ventana hasta que el sub array sea invalido la cantidad de sub arrays validos es 4
  [1,3,2,3,3] -> [3,2,3,3] -> [2,3,3] -> [3, 3]
    
Si sumamos los anteriores sub-arrays (son distintos) 2 + 4 => la respuesta da 6

Pero no es necesario empezar desde 0 cada vez, podemos aprovecharnos de que ya calculamos cuantos subarrays validos siempre que se cumple
la condicion del while y al final sumarle left al final

El truco para entender esto es siempre pararte en el indice i donde se cumpla la condicion y hacer el ejercicio de contar cuantos sub-arrays validos hay
Luego sumar todo y estamos
'''
            


