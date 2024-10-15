# Realizar un programa que pida la calificación final de fund. de programación
# Considere el escenario donde 'esta reprobado': 0 < cal < 69
# 'Alcanzo el minimo para pasar': cal == 70
# 'Aprobo excelente mente': cal == 100
# Imprima que paso en todos los casos 'Aprobo': 70 < cal < 100
# En un caso no contemplado: valor no validoif #

calificacion = int(input("Ingrese calificacion"))

if calificacion >= 0 and calificacion < 70:
    print("Está reprobado")
elif calificacion >= 70 and calificacion <= 100:
    print("Aprobo")
    if calificacion == 70:
        print("Pasó de pambazo :)")
    elif calificacion == 100:
        print("aprobo excelentemente")
else:
    print("Error")
