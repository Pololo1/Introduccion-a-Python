'''
TIPOS DE DATOS
String : cadenas de texto ""  o ''
int
float
boolean

ESTRUCTURAS DE DATOS
sets : {} instanciamos con new Set
    nos riven para almacenar datos únicos

listas : [] instanciamos con new List
tuplas: () instanciamos con tuple 
diccionarios {clave1:valor1, clave2:valor2, claveN:valorN} instanciamos con Dict
'''


conjunto={1,999,3,5,6,9,2}
#print(conjunto)

conjunto2 = {5,10,"2",3,6,9}

#Metodos: ¿Qué ódemos hacer con los objetos?

conjunto.add(8)
#print(conjunto)

conjunto.pop()
#print(conjunto)

#print("INTERSECTION: ",conjunto.intersection(conjunto2))
#print("UNION: ", conjunto.union(conjunto2))


#Tuplas:

tupla1=(4,5,"9",5)
tupla2=(3,9,"uv")

#print(type(tupla1))
#print(tupla1)

#print(tupla1.count(5)) #veces que sale el 5
#print(tupla1.index(5)) #return first index

#LISTAS:
lista1=[True,10, "true", 5, "b", 10]
#print(type(lista1))
#print(lista1.sort())

#DICCIONARIOS:
usuario1={"nombre":"Santiago","email":"santiago.polo@correounivalle.edu.co","apellido":"Polo", "estudiante":True}
# Muestra las llaves (keys)
#print("Claves:", usuario1.keys())  
# 👉 Devuelve una vista con todas las claves del diccionario

# Muestra los valores
#print("Valores:", usuario1.values())  
# 👉 Devuelve una vista con todos los valores

# Muestra items (pares clave: valor)
#print("Items:", usuario1.items())  
# 👉 Devuelve tuplas con clave y valor

# Obtener valor con get()
#print("Get nombre:", usuario1.get("nombre"))  
# 👉 Devuelve el valor de la clave si existe, si no retorna None (o el valor por defecto que especifiques)

# Establecer valor si no existe con setdefault()
#print("Setdefault:", usuario1.setdefault("edad", 23))  
# 👉 Si "edad" no existe, la agrega con valor 23; si existe, devuelve su valor

# Copiar diccionario
usuario_copia = usuario1.copy()
#print("Copia:", usuario_copia)  
# 👉 Crea una copia independiente del diccionario

# Actualizar con update()
usuario1.update({"ciudad": "Palmira"})
#print("Update:", usuario1)  
# 👉 Agrega o modifica claves con un nuevo diccionario

# Eliminar con pop()
usuario1.pop("apellido")
#print("Pop (apellido eliminado):", usuario1)  
# 👉 Elimina la clave indicada y devuelve su valor

# Eliminar último elemento con popitem()
usuario1.popitem()
#print("Popitem (último eliminado):", usuario1)  
# 👉 Elimina el último par clave-valor insertado

# Crear diccionario con fromkeys()
nuevo = dict.fromkeys(["a", "b", "c"], 0)
#print("Fromkeys:", nuevo)  
# 👉 Crea un diccionario con esas claves y valor inicial (a:0, b:0, c:0)

# Limpiar todo con clear()
usuario1.clear()
#print("Clear:", usuario1)  
# 👉 Deja el diccionario vacío

#Acceder a la información:
lista_=[5,3,9,10,9,12,"true"]
#print(lista_[2:])
#print(lista_[:])
#print(lista_[-4:-1])

tupla20=(2,9,5,6,"uv")
#print(tupla20[2])

curso={"NOMRE":"TDMI", "cantidad":20,"cancelar":"si"}
print(curso["cantidad"])
curso["cancelar"]="No"
print(curso)