#Ejercicio 1
b1 = input("Debera ingresar 4 marcas de bebidas, ingrese la primera: ")
b2 = input("ingrese la segunda: ")
b3 = input("ingrese la tercera: ")
b4 = input("ingrese la cuarta: ")

l1 = [b1,b2,b3,b4]
print(l1)
u = l1[0]
p = l1[-1]
print(u,p)

#Ejercicio 2
print("Ingrese la fecha de vencimiento de 3 productos")
p1 = int(input("\nIngrese el día del primer producto: ")), int(input("Ingrese el mes: ")), int(input("Ingrese el año: "))
p2 = int(input("\nIngrese el día del segundo producto: ")), int(input("Ingrese el mes: ")), int(input("Ingrese el año: "))
p3 = int(input("\nIngrese el día del tercer producto: ")), int(input("Ingrese el mes: ")), int(input("Ingrese el año: "))

fv = (p1, p2, p3)

of = print(sorted(fv))

#Ejercicio 2
print()