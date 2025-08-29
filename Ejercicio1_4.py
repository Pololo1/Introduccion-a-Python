'''
Escriba un programa que capture del usuario dos valores a y b en dos inputs sucesivos. 
Pida al usuario desde la función input que los valores a ingresar deben contener al 
menos un número decimal. Al ejecutar, el programa debe realizar la multiplicación 
entre los dos valores y entregar la respuesta en un formatted string que 
contenga una variable llamada resultado y el texto de su preferencia
'''
a= float(input("Digite el valor de a con al al menos un decimal: "))
b= float(input("Digite el valor de b con al al menos un decimal: "))
c=a*b
print(f"El resultado de la multiplicación es {c}")

