#1
tex = """La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional 
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus 
pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion
democratica."""
tex = tex.lower()
ctex = tex.count("universidad")

tuplatex = ("universidad",) * ctex
print(f"La cantidad de veces que se repite la palabra 'universidad' son {ctex} veces")
print(f"La palabra encontrada es: '{tuplatex}'")