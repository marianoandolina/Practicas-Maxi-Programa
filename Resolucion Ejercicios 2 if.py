# PREEJERCICIO 1

# Ingresamos un programa que nos diga si la persona es mayor de edad. En este caso 21 años.

# edad= int(input("Ingrese la edad: "))
# if edad >= 21:
#     print("La persona es mayor de edad")
# else:
#     print("La persona es menor de edad")

#PREEJERCICIO 2

# print("A continuacion le pedimos que ingrese dos numeros distintos.")
# n1= int(input("Ingrese el primer numero: "))
# n2= int(input("Ingrese el segundo numero, (recuerde qe sea distinto al primero): "))

# if n1>n2:
#     r= n1 - n2
#     print(f"El resultado de la resta de el mayor con el menor es {r}")
# else:
#     r= n2 - n1
#     print(f"El resultado de la resta de el mayor con el menor es {r}")

# Hacer	un	programa	para	ingresar	un	número	y	luego	se	emita	por	pantalla	un	
# cartel	aclaratorio	si	“Es	mayor	a	10”	o	“No	es	mayor	a	10”.

# n1= int(input("Ingrese un numero: "))

# if n1>10:
#     print("El numero es mayor a 10")
# else:
#     print("No es mayor a 10")

# Hacer	un	programa	para	ingresar	dos	números	distintos	y	luego	se	muestre	por	
# pantalla	el	menor	de	ellos.	

# n1= int(input("Ingresa un numero: "))
# n2= int(input("Ingresa otro numero distinto al anterior: "))

# if n1<n2:
#     print(n1)
# else:
#     print(n2)    3

#  Hacer	un	programa	para	ingresar	dos	números	y	que	luego	emita	por	pantalla	
# el	mayor	de	ellos	o	un	cartel	aclaratorio	“Son	iguales”	en	el	caso	de	que	así	sea.

# n1= int(input("Ingrese un numero: "))
# n2= int(input("Ingrese otro numero: "))

# if n1>n2:
#     print(n1)
# elif n1<n2:
#     print(n2)
# if n1==n2:
#     print("Son Iguales")

# Hacer	un	programa	para	ingresar	un	número	y	luego	se	emita	un	cartel	por	
# pantalla	“Positivo”	si	el	número	es	mayor	a	cero,	“Negativo”	si	el	número	es	
# menor	a	cero	o	“Cero”	si	el	número	es	igual	a	cero.	

# n1= int(input("Ingresa un numero: "))

# if n1>0:
#     print("Positivo")
# elif n1<0:
#     print("Negativo")
# else:
#     print("Cero")

#Ejercicio Practico --- Ingresar 3 numeros y que muestre siempre el mayor de los 3. 

# a= int(input("Ingrese un numero: "))
# b= int(input("Ingrese un numero: "))
# c= int(input("Ingrese un numero: "))

# if a>b:
#     if a>c:
#         print(f"El mayo de todos es {a}")
# elif b>c:
#     print(f"El mayor es {b}")
# else:
#     print(f"El mayor es {c}")

## EJERCICIO PROPIO, INGRESAR 2 NOTAS Y QUE MUESTRE EL CARTEL DE "APROBADO" SI EL PROMEDIO DE AMBAS ES IGUAL O MAYOR A 7.

# nota_1= int(input("Ingrese la nota de Matematica: "))
# nota_2= int(input("Ingrese la nota de Algebra: "))

# promedio= (nota_1 + nota_2) / 2

# if promedio >= 7:
#     print(f"Tu promedio es {promedio} por lo tanto aprobaste.")
# else:
#     print(f"Tu promedio es {promedio} por lo tanto no estas aprobado.")    

#EJERCICIO "Ingresar importe, si es menor a $1000 no tiene descuento, entre 1000 y 5000 tiene un 10% de descuento y mayor a 5000 tiene un 15% de descuento"

# importe= int(input("Ingrese el importe total de la compra: "))

# if importe > 1000 and importe < 5000:
#     total= importe * 0.90
#     print(f"El total con el descuento es {total}")
# elif importe > 5000:
#     total= importe * 0.85 
#     print(f"El total con el descuento es {total}")
# else:
#     print(f"El total es {importe}")

# EJERCICIO "Ingresar 4 numero e y mostrar por pantalla cuantos son menores a 100"

# numero_1= int(input("Ingresa el nro 1: "))
# numero_2= int(input("Ingresa el nro 2: "))
# numero_3= int(input("Ingresa el nro 3: "))
# numero_4= int(input("Ingresa el nro 4: "))

# mayores= int(0)

# if numero_1>100:
#     mayores += int(1)
# if numero_2>100:
#     mayores += int(1)
# if numero_3>100:
#     mayores += int(1)
# if numero_3>100:
#     mayores += int(1)

# print(mayores)


