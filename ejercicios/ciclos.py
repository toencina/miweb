import os
import time 

#___________________ VARIABLES __________________
cant_usuarios_atendidos=0
edad=0
sexo="F"
tiempo_para_jubilar=0
peso=0
estatura=0
imc=0

#============================= CODIGO PRINCIPAL ========================================
while True:
    os.system("cls")
    print('''
          ------ MENÚ -----
          1.- Calcular años para jubilación
          2.- Calcular IMC
          3.- Cantidad de usuarios atendidos
          4.- Salir    ''')
    opcion_menu= int(input("\nIngrese opción:  "))
    
    if opcion_menu==1:
        os.system("cls")
        print(" ============ Años para jubilar ==============")
        edad = int(input("Ingrese edad: "))
        sexo = input("Ingrese su sexo: F/M  ").upper()
        if sexo=="F":
            tiempo_para_jubilar= 60-edad
        else:
            tiempo_para_jubilar=65-edad
        
        print(f"\nA usted le faltan: {tiempo_para_jubilar} años")    
        cant_usuarios_atendidos = cant_usuarios_atendidos+1    
        os.system("pause")
        
    if opcion_menu==2:
        os.system("cls")
        print("========== CALCULO DEL IMC ===========")
        peso = float(input("Ingrese peso(Kg.): "))
        estatura = float(input("Ingrese su estatura (m.):   "))
        imc= peso/estatura**2
        
        print(f"\nSu IMC es de {imc} ")
        cant_usuarios_atendidos = cant_usuarios_atendidos+1
        os.system("pause")
    
    if opcion_menu==3:
        os.system("cls")
        print(" ============ Estadísticas ==============")
        print(f"Cantidad de personas atendidas: {cant_usuarios_atendidos}")
        os.system("pause")
        
    if opcion_menu==4:
        os.system("cls")
        print("Saliendo de la app...")
        time.sleep(1.5)     
        break