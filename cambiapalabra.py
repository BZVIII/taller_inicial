import sys

argumentos = sys.argv

nombreF = argumentos[1]
original = argumentos[2]
nueva = argumentos[3]


f = open(nombreF, "r")  

texto_original = f.read()
f.close()

texto_sustituido = texto_original.replace(original, nueva)

f = open(nombreF, "w")
f.write(texto_sustituido)
f.close()