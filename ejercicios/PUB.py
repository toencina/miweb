import os
print("-----Bienvenido al PUB LA VIRGEN digite el bebestible que desea-----")
valor= 0
opcion = 0
producto = 0
cantidad = 0
happy = 0
total= 0
subtotal = 0
opcion= int(input('''                        1.- VODKA TONICA
                        2.- RON COLA
                        3.- CERVEZA
                        4.- BEBIDA
                               '''))
while opcion<1 or opcion>4:
    opcion=int(input("Ingrese opcion valida: "))

cantidad = int(input("¿Cuantas pintas desea?:  "))

if opcion==1:
    valor= 5500
    producto = "Vodka tónica"
if opcion==2:
    valor = 5000
    producto = "Ron cola"
if opcion==3:
    valor = 2000
    producto = "Cerveza"
if opcion==4:
    valor =1500
    producto = "Bebida"
else:("numero no valido")  

happy = str(input("Estamos en happy hour  S/N:  ")).upper()
while happy!="S" or happy!="N":
    happy = str(input("Por favor indique si estamos en happy hour S/N:  ")).upper()
    if happy=="S":
        subtotal= valor*cantidad 
        total = (subtotal/2)
        os.system("cls")
        print(f'''---------------BOLETA---------------
                Producto:             {producto}
                Valor:               ${valor}
                Cantidad:             {cantidad}
                Descuento happy hour: {happy}
                Subtotal:            ${total}
                Total:               ${total/2} 
            --------GRACIAS POR VENIR A BAR LA VIRGEN-------''')
        break
    elif happy == "N":
        subtotal= valor*cantidad
        total = subtotal
        os.system("cls")
        print(f'''---------BOLETA---------
                Producto:             {producto}
                Valor:               ${valor}
                Cantidad:             {cantidad}
                Descuento happy hour: {happy}
                Subtotal:            ${total}
                Total:               ${total} 
            --------GRACIAS POR VENIR A BAR LA VIRGEN-------''')
        break



    