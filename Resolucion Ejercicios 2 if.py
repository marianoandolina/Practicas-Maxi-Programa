#Ejercicio 1
# Ingresamos un programa que nos diga si la persona es mayor de edad. En este caso 21 años.

# edad= int(input("Ingrese la edad: "))
# if edad >= 21:
#     print("La persona es mayor de edad")
# else:
#     print("La persona es menor de edad")

#Ejercicio 2

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

n1= int(input("Ingrese un numero: "))

if n1>10:
    print("El numero es mayor a 10")
else:
    print("No es mayor a 10")
