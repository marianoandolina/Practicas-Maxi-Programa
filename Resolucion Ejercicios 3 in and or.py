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
# else n1<n2:
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

litros_vendidos= int(input("Cuantos litros se vendieron: "))
valor_litro= int(12)
importe= litros_vendidos*valor_litro

if litros_vendidos<100:
    print(f"El importe total es {importe}, no se aplica descuento")
if litros_vendidos>100 and litros_vendidos<301:
    importe_final= importe * 0.90
    print(f"El importe con el descuento es de {importe_final} pesos")
if litros_vendidos>300 and litros_vendidos<501:
    importe_final= importe * 0.85
    print(f"El importe con el descuento es de {importe_final} pesos")
if litros_vendidos>500:
    importe_final= importe * 0.75
    print(f"El importe con el descuento es de {importe_final} pesos")          

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

'''---> 6. Hacer un programa para ingresar por teclado la longitud de los tres lados de un
triángulo y que luego determine e informe con un cartel aclaratorio a qué tipo
de triángulo corresponde:
a. Equilátero: cuando los tres lados sean iguales.
b. Isósceles: cuando dos de los tres lados sean iguales.
c. Escaleno: cuando todos los lados sean distintos.'''

# lado_a= int(input("Ingrese el lado a del triangulo: "))
# lado_b= int(input("Ingrese el lado b del triangulo: "))
# lado_c= int(input("Ingrese el lado c del triangulo: "))

# if lado_a==lado_b and lado_a==lado_c and lado_b==lado_c:
#     print("Es un triangulo Equilatero")
# if (lado_a==lado_b and lado_a!=lado_c) or (lado_b==lado_c and lado_c!=lado_a) or (lado_c==lado_a and lado_c!=lado_b):
#     print("Es un triangulo Isoceles")
# if lado_a!=lado_b and lado_a!=lado_c and lado_b!=lado_c:
#     print("El triangulo es Escaleno")

''' ---> 7. Hacer un programa para ingresar 4 números. Luego analizar e informar por
pantalla si los mismos se encuentran ordenados de forma decreciente.'''

# num_1= int(input("Ingrese el primer numero: ")) 
# num_2= int(input("Ingrese el segundo numero: "))
# num_3= int(input("Ingrese el tercer numero: "))
# num_4= int(input("Ingrese el cuarto numero: "))

# if num_1>num_2 and num_2>num_3 and num_3>num_4:
#     print("Estan ordenados decrecientemente")
# else:
#     print("No estan ordenados decrecientemente.")
 
'''8. El negocio de desinfectante antes mencionado vende además detergente
suelto, y los precios se aplican según la siguiente escala:
a. 25 ARS por litro los primeros 50 litros.
b. 20 ARS por litro si la venta es de 51 a 200 litros.
c. 15 ARS por litro si la venta es de 201 a 500 litros.
d. 10 ARS por litro si la venta es de más de 500 litros.
Además, si paga en efectivo, tiene un adicional del 10% sobre el importe final.
Hacer un programa que solicite la cantidad de litros vendidos y el tipo de pago
(ingresará 1 si paga en efectivo y 0 con cualquier otro medio de pago) y calcule
y emita por pantalla el monto final a abonar por el cliente.'''


# lts= int(input("Ingrese los litros vendidos."))
# pago= int(input("Ingrese la forma de pago 1 para efectivo, 0 para cualquier otro medio de pago."))
# valor_del_litro= int(0)

# if lts<50 and pago==1:
#     valor_del_litro= int(25)
#     total= (lts*valor_del_litro)*0.90
#     print(f"El total es {total} pesos")
# elif lts<50 and pago==0:
#     valor_del_litro= int(25)
#     total= (lts*valor_del_litro)
#     print(f"El total es {total} pesos")

# if lts>50 and lts<200 and pago==1:
#     valor_del_litro= int(20)
#     total= (lts*valor_del_litro)*0.90
#     print(f"El total es {total} pesos")
# elif lts>50 and lts<200 and pago==0 : 
#     valor_del_litro= int(20)
#     total= (lts*valor_del_litro)
#     print(f"El total es {total} pesos")

# if lts>199 and lts<500 and pago==1:
#     valor_del_litro= int(15)
#     total= (lts*valor_del_litro)*0.90
#     print(f"El total es {total} pesos")
# elif lts>199 and lts<500 and pago==0:
#     valor_del_litro= int(15)
#     total= (lts*valor_del_litro)
#     print(f"El total es {total} pesos")

# if lts>499 and pago==1:
#     valor_del_litro= int(10)
#     total= (lts*valor_del_litro)*0.90
#     print(f"El total es {total} pesos")
# elif lts>499 and pago==0:
#     valor_del_litro= int(10)
#     total= (lts*valor_del_litro)
#     print(f"El total es {total} pesos")


    





