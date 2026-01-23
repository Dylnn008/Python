#Cifrado Cesar 
#Crear uan funcion que permita cifrar un texto utilizando el cifrado Cesar
def cifrar_cesar(texto, nume_de_desplazamiento):
    Abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    texto = input(str("Ingrese el texto a cifrar: ")).upper()
    nume_de_desplazamiento = int(input("Ingrese el numero de desplazamiento: "))
    texto_cifrado = Abecedario[nume_de_desplazamiento:] + Abecedario[:nume_de_desplazamiento]
    tabla_de_traduccion = str.maketrans(Abecedario, texto_cifrado)
    texto_cifrado = texto.translate(tabla_de_traduccion)
    return texto_cifrado
print("Texto cifrado: ", cifrar_cesar("",""))