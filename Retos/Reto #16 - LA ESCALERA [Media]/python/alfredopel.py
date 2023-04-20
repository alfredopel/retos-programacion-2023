"""
 Crea una función que dibuje una escalera según su número de escalones.
 - Si el número es positivo, será ascendente de izquiera a derecha.
 - Si el número es negativo, será descendente de izquiera a derecha.
 - Si el número es cero, se dibujarán dos guiones bajos (__).
 
 Ejemplo: 4
         _
       _|       
     _|
   _|
 _|
"""

num=int(input("Escribe un número:"))

i=0

if (num > 0):
    blank = "  "*num
    print(f'{blank}_')
    while i < num:
        i+=1
        blank= "  "*(num-i)
        print(f'{blank}_|')
elif (num < 0):
    print("_")
    blank=" "
    while i >num:
        print(f"{blank}|_")
        blank+="  "
        i-=1
else:
    print("__")