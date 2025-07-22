import os

nota = int(input("Ingresar nota"))


if nota < 7 :
    print("Desaprobo insta")
elif nota >= 7 and nota < 10 :
    print("Buena aprobardo")
else:
    print("Exelente papu")


es_fin_de_semana = False

if not es_fin_de_semana :
    print("A laburar mamasa")