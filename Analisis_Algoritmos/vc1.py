# Escribe aquí tu respuesta con los comentarios que sean necesarios para que el código sea claro
max_iteracion = 220
'''
Hacemos la función 'function_complex' que recibe dos parámetros, los cuáles se definen como se ve en la 
definición de arriba.
'''
def function_complex(z,c):
    return z**2 + c 

'''
Genereamos los primeros n términos de la sucesión haciendo recursión sobre nuestra función 'sucesion_terms'.
'''
def sucesions_terms(z,c,n,list_storage):
    list_storage.append(z)
    if n == 0:
        list_storage
    else:
        z = function_complex(z,c)
        list_storage = sucesions_terms(z,c,n-1,list_storage)
    list_terminos = list_storage
    return list_terminos
print(sucesions_terms(complex(1),complex(1),4,[]))
print(sucesions_terms(complex(0,1),complex(0,1),4,[])) 
print(sucesions_terms(complex(24),complex(24),4,[]))
''' 
Para fines prácticos, digamos que c viene en tupla si tenemos al complejo x+yj con 'y' distinto de cero, es decir, 
pondremos (x,y), y si 'y' es cero, entonces lo insertamos como parámetro, es decir, sólo 'x' 
''' 
def sucesion_convergence(c,n): 
    try:
        if len(c) == 2:
            i,j = c
            complex_number = complex(i,j)
#            return complex_number
    except: 
        complex_number = complex(c)
#        return complex_number
    
    #Ahora hagamos una recursión aplicando 'sucesions_terms' para obtener los n valores de la sucesion
    complex_copy = complex_number
    function = sucesions_terms(complex_number, complex_copy, n)
    
    return function

