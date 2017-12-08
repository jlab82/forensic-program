# coding: utf-8
# Programa que encontrará al ladrón de helado

hair_color = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC",}
facial_shape = {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA",}
eye_color = {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC",}
gender = {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC",}
race = {"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}

Eva = [gender["female"], race["white"], hair_color["blonde"], eye_color["blue"], facial_shape["oval"],]
Larisa = [gender["female"], race["white"], hair_color["brown"], eye_color["brown"], facial_shape["oval"],]
Matej = [gender["male"], race["white"], hair_color["black"], eye_color["blue"], facial_shape["oval"],]
Miha = [gender["male"], race["white"], hair_color["brown"], eye_color["green"], facial_shape["square"],]

Sospechosos = [Eva, Larisa, Matej, Miha]
Nombres = ["Eva", "Larisa", "Matej", "Miha"]

#función de búsqueda en fichero de texto
def match (sospechoso):
    cont = 0
    import re
    f = open("dna.txt", "r")
    valor = f.read()
    for dna in sospechoso:
        if re.findall(dna, valor):
            cont = cont + 1
    f.close()
    return cont
#Mostrar posibilidades de cada sospechoso
i = 0
for dna in Sospechosos:
    print Nombres[i] + " con DNA " + str(dna) + " tiene " + str(match (dna)) + " de 5 posibilidades de ser el ladrón de donuts"
    i = i + 1

