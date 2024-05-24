d1 = input("Ingrese la descripcion del primer producto, recuerde que no debe tener mas de 40 caracteres")
d_p1 = d1[:40]
longitud = len(d1) > 40
p1 = int(input("Ingrese el valor en CPL"))
ca1 = int(input("Ingrese la cantidad que queda del producto"))

d2 = input("Ingrese la descripcion del segundo producto, recuerde que no debe tener mas de 40 caracteres")
d_p2 = d2[:40]
longitud = len(d2) > 40
p2 = int(input("Ingrese el valor en CPL"))
ca2 = int(input("Ingrese la cantidad que queda del producto"))



vtp = p1 + p2
vtc = ca1 + ca2 
vt = vtc + vtp

print(f"El valor total del inventario de todos los productos {vt} CLP")

print(f"El precio promedio es de {} CLP")