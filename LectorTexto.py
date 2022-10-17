#ingresar palabra a buscar
Palabra = input("Ingresa la palabra que deseas buscar: ")

#leer archivo txt
archivo = open("texto.txt", "r")
i=0
acumulador = 0

for line in archivo.readlines():
    Lista_por_puntos = line.split(".")
    texto_sin_puntos = " ".join(Lista_por_puntos)
    Lista_sin_comas = texto_sin_puntos.split(",")
    texto_sin_comas = " ".join(Lista_sin_comas)
    Lista = texto_sin_comas.split()
    i=Lista.count(Palabra)
    acumulador = acumulador + i


if acumulador !=1:
    print("En el texto la palabra: " + Palabra + " se repite " + str(acumulador) + " veces")
else:
    print("En el texto la palabra: " + Palabra + "se repite " + str(acumulador) + " vez")


archivo.close()
