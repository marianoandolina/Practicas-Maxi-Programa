''' 1. --- Hacer un programa que solicite el ingreso de un número y que luego emita un
cartel por pantalla aclarando si el mismo es múltiplo de 5.'''

# numero= int(input("Ingresa un numero: "))

# esmul= numero%5

# if esmul == 0:
#     print("Es multiplo de 5")
# else:
#     print("No es multiplo de 5")

''' 2. --- Hacer un programa que solicite el ingreso de dos números y luego calcular:
a. La resta si el primero es mayor que el segundo.
b. La suma si son iguales.
c. El producto si el primero es menor.
Se deberá emitir un cartel por pantalla con el resultado correspondiente.'''

# n1= int(input("Ingrese el primer numero: "))
# n2= int(input("Ingrese el segundo numero: "))

# if n1>n2:
#     resta= n1 - n2
#     print(resta)
# if n1==n2:
#     suma= n1 + n2
#     print(suma)
# if n1<n2:
#     producto= n1*n2
#     print(producto)    

'''  3. --- Hacer un programa para ingresar dos números. Si el segundo es distinto de
cero, calcular la división del primero por el segundo y mostrar el resultado por
pantalla; caso contrario, emitir un cartel aclarando que no se puede dividir por
cero.'''

# n1= int(input("Ingrese el primer numero: "))
# n2= int(input("Ingrese el segundo numero: "))

# if n2 != int(0):
#     dividir= n1/n2
#     print(dividir)
# else:
#     print("No se puede divir por cero")

'''4. --- Un importante negocio de desinfectante líquido realiza descuentos
dependiendo de la cantidad de litros vendidos según la siguiente escala:
a. Si vende menos de 100 litros, no hay descuento.
b. Si vende entre 101 y 300 litros, el descuento es del 10%.
c. Si vende entre 301 y 500 litros, el descuento es del 15%.
d. Finalmente, si la venta es de más de 500 litros, el descuento es del 25%.
Hacer un programa que solicite el ingreso del importe total de la venta y la
cantidad de litros vendidos y calcule y emita el importe con el descuento
aplicado.'''

# litros_vendidos= int(input("Cuantos litros se vendieron: "))
# valor_litro= int(12)
# importe= litros_vendidos*valor_litro

# if litros_vendidos<100:
#     print(f"El importe total es {importe}, no se aplica descuento")
# if litros_vendidos>100 and litros_vendidos<301:
#     importe_final= importe * 0.90
#     print(f"El importe con el descuento es de {importe_final} pesos")
# if litros_vendidos>500:
#     importe_final= importe * 0.85
#     print(f"El importe con el descuento es de {importe_final} pesos")          

'''5. --- Hacer un programa que solicite el ingreso de las notas del primer parcial y del
segundo parcial de una alumna de programación. El programa deberá analizar
las notas y emitir la situación de la alumna según la siguiente escala:
a. Si tiene 8 o más en ambos parciales, emitir “aprobación directa”.
b. Si no tiene 8 o más en ambos pero tiene aprobados ambos parciales (se
aprueba con 6 o más), emitir “rinde examen final”.
c. Si tiene menos de 6 en alguno de los dos parciales, emitir “debe
recuperar”.
El programa debe emitir solo un cartel, el que corresponda.'''

# nota_1= int(input("Ingrese la nota del primer parcial: "))
# nota_2= int(input("Ingrese la nota del segundo parcial: "))

# if nota_1>=8 and nota_2>=8:
#     print("Directamente aprobada")
# if (nota_1>=6 and nota_1<=7) and (nota_2>=7 and nota_2<=7):
#     print("Rinde el examen final")
# if nota_1<6 or nota_2<6:
#     print("Debe recueperar")




