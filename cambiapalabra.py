import sys

argumentos = sys.argv

while len(argumentos) < 4:
    if len(argumentos) < 2:
        p = input("Nombre de fichero: ")
        if len(p) == 0:
            continue
        argumentos.append(p)

    if len(argumentos) < 3:
        p = input("palabra original: ")
        if len(p) == 0:
            continue
        argumentos.append(p)

    if len(argumentos) < 4:
        p = input("nueva palabra: ")
        if len(p)== 0:
            continue
        argumentos.append(p)


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