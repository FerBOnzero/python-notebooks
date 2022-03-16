# Escribe aquí tu respuesta con los comentarios que sean necesarios para que el código sea claro
max_iteracion = 220
def function_fc(z):
    return z**2
print('function fc: ', function_fc(complex(4))

''' 
Para fines prácticos, digamos que c viene en tupla si tenemos al complejo x+yj con 'y' distinto de cero, es decir, 
pondremos (x,y), y si 'y' es cero, entonces lo insertamos como parámetro, es decir, sólo 'x' 
''' 
def sucesion_zcn(c,n): 
    try:
        if len(c) == 2:
            i,j = c
            complex_number = complex(i,j)
#            return complex_number
    except: 
        complex_number = complex(c)
#        return complex_number
    
    #Ahora hagamos una recursión aplicando 'function_fc' para obtener los n valores de la sucesion
    
    function = function_fc(complex_number) + complex_number
      
print(sucesion_zcn((2,1),10))
print(sucesion_zcn(24,10))