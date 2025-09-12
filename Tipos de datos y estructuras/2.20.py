"""
Ejercicio 2.20
Para la construcción de una aplicación de notas escolares es necesario crear una base de datos con los nombres 
de los estudiantes y la nota obtenida en un curso. Para almacenar los datos se le ha pedido que cree un 
diccionario donde las claves sean los nombres de los estudiantes y los valores sean las notas obtenidas. 

Para efectos de desarrollar los siguientes ejercicios se definirá el diccionario como calificaciones. 
Una vez creado compruebe el tipo de objeto que queda almacenado en la variable calificaciones. Utilice para esto la función type
"""

calificaciones={"Liliana":4.5,
       "Carmen":3.3,
       "Josefina":4.1,
       "Daniela":4.9,
       "Pedro":2.9,
       "José":4.6,
       "Mario":3.3}
print(type(calificaciones))

"""
Ejercicio 2.21
Aplique la función sorted sobre el diccionario calificaciones. Discuta la necesidad de usar esta función en el diccionario analizado.
"""
print(sorted(calificaciones.values(), reverse = True)) 
#Permite ordenar por las keys o valores

"""
Ejercicio 2.22
Parece ser que el método pop permite eliminar un elemento de un diccionario. 
Ejecute la siguiente instrucción:
>>> calificaciones.popitem({'Daniela': 4.9})
¿Qué interpretación se le puede dar al mensaje de error que nos entrega el intérprete cuando ejecutamos?:
TypeError: popitem() takes no arguments (1 given)
¿Cuándo es conveniente aplicar este método?
"""
print(calificaciones.popitem())
#El método popitem no admite argumentos, elimina, por defecto, el último elemento de diccionario, por ello es que sale ese tipo de error
#Es conveniente usar cuando somos consientes de el último elemento y queremos eliminarlo

"""
Ejercicio 2.23 
Utilice el método ítems sobre el diccionario. ¿qué retorna este método?, 
¿qué tipo de estructura de datos parece, una lista?, una lista de listas?, 
¿una lista de tuplas?. Investigue para más información sobre los objetos de tipo dict_items.
"""
print(calificaciones.items())
#El método retorna todos los elementos (con key y value) del diccionario
#aparece una lista de tuplas, es decir, corchetes que agrupan todos los elementos y parentesis con cada elemento

"""
Ejercicio 2.24
Sobre el diccionario calificaciones aplique el método update verificando los argumentos necesarios para el
correcto funcionamiento si se quiere modificar la nota asignada a la estudiante Liliana a un valor de 4.7.
"""
nueva= {"Liliana":4.7}
calificaciones.update(nueva)
print(calificaciones)