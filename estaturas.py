estatura = int(input("Ingrese su estatura"))

if estatura <= 150:
    print("Eres bajito")
elif estatura > 150 and estatura <= 170:
    print("Eres estatura promedio")
elif estatura > 170:
    print("Eres alto")
else:
    print("Error")

