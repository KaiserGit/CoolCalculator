# ^ SIMPLES PRUEBAS PARA INTENTAR GENERAR INTERFACES GRAFICAS, NO ES PARA USAR AHORA ^
# El verdadero codigo empieza aqui abajo

import math

menu = True

print("--Bienvenido a la calculadora de FISICA V.Beta-1.0--")
print("Programada por: Camilo Rodriguez 5°C IDAP")
while menu == True:
    print("Elige una opcion")

    print("1-MRU")

    print("2-MRUV")

    print("3-MCL (MODO EXPERIMENTAL)")

    print("4-Finalizar")

    eleccion = float(input("Escribe tu eleccion: "))

    if eleccion == 1:
        print("Perfecto, ha elegido MRU")
        print("Por favor, introduzca los datos de los que dispone, en el caso de no tenerlos introduzca -")
        Vm_MRU = input("Velocidad Media: ")
        T_MRU = input("Tiempo: ")
        D_MRU = input("Desplazamiento: ")
# Esto lo que hace es analizar si se tienen o no los datos suficientes, en caso de no disponerse, no se da resultado
        if Vm_MRU == "-":
            Vm_MRUinvalid = 1
        else:
            Vm_MRUinvalid = 0
        if D_MRU == "-":
            D_MRUinvalid = 1
        else:
            D_MRUinvalid = 0
        if T_MRU == "-":
            T_MRUinvalid = 1
        else:
            T_MRUinvalid = 0
        if D_MRUinvalid + T_MRUinvalid + Vm_MRUinvalid > 1:
            print("No hay suficientes datos para realizar calculos")
        elif D_MRUinvalid + T_MRUinvalid + Vm_MRUinvalid == 0:
            print("No ha introducido correctamente")
        elif D_MRUinvalid + T_MRUinvalid == 0:
            FloatD_MRU = float(D_MRU)
            FloatT_MRU = float(T_MRU)
            ResultadoMRU = FloatD_MRU / FloatT_MRU
            print("El resultado es: " + str(ResultadoMRU) + "m/s")
        elif D_MRUinvalid + Vm_MRUinvalid == 0:
            FloatD_MRU = float(D_MRU)
            FloatVm_MRU = float(Vm_MRU)
            ResultadoMRU = FloatD_MRU / FloatVm_MRU
            print("El resultado es: " + str(ResultadoMRU) + "s")
        elif Vm_MRUinvalid + T_MRUinvalid == 0:
            FloatT_MRU = float(T_MRU)
            FloatVm_MRU = float(Vm_MRU)
            ResultadoMRU = FloatT_MRU * FloatVm_MRU
            print("El resultado es: " + str(ResultadoMRU) + "m")

    elif eleccion == 2:
        print("Perfecto, ha elegido MRUV")
        print("Por favor, introduzca los datos de los que dispone, en el caso de no tenerlos introduzca -")
        Vi_MRUV = input("Velocidad Inicial: ")
        Vf_MRUV = input("Velocidad final: ")
        T_MRUV = input("Tiempo: ")
        D_MRUV = input("Desplazamiento: ")
        A_MRUV = input("Aceleracion: ")

        if Vi_MRUV == "-":
            Vi_MRUVinvalid = 1
        else:
            Vi_MRUVinvalid = 0
        if Vf_MRUV == "-":
            Vf_MRUVinvalid = 1
        else:
            Vf_MRUVinvalid = 0
        if D_MRUV == "-":
            D_MRUVinvalid = 1
        else:
            D_MRUVinvalid = 0
        if T_MRUV == "-":
            T_MRUVinvalid = 1
        else:
            T_MRUVinvalid = 0
        if A_MRUV == "-":
            A_MRUVinvalid = 1
        else:
            A_MRUVinvalid = 0
        if D_MRUVinvalid + T_MRUVinvalid + Vi_MRUVinvalid + Vf_MRUVinvalid + A_MRUVinvalid > 2:
            print("No se han introducido datos suficentes")
        elif D_MRUVinvalid + T_MRUVinvalid + Vf_MRUVinvalid + Vi_MRUVinvalid + A_MRUVinvalid == 0:
            print("No ha introducido los datos correctamente")

# Datos de prueba: Vi = 0 / Vf = 20 / T = 2 / D = 20 / A = 10

# Si tiene 3 datos va a usar las primeras ecuaciones
        elif D_MRUVinvalid + T_MRUVinvalid + Vi_MRUVinvalid + Vf_MRUVinvalid + A_MRUVinvalid == 2:
            if D_MRUVinvalid + T_MRUVinvalid + Vi_MRUVinvalid == 0:
                FloatD_MRUV = float(D_MRUV)
                FloatT_MRUV = float(T_MRUV)
                FloatVi_MRUV = float(Vi_MRUV)
                FloatA_MRUV = ((FloatD_MRUV - FloatVi_MRUV * FloatT_MRUV) / (FloatT_MRUV**2)) / 0.5
                FloatVf_MRUV = (FloatD_MRUV / FloatT_MRUV) / 0.5 - FloatVi_MRUV
                print("La aceleracion es: " + str(FloatA_MRUV) + "m/s²")
                print("La velocidad final es: " + str(FloatVf_MRUV) + "m/s")
            elif D_MRUVinvalid + Vi_MRUVinvalid + A_MRUVinvalid == 0:
                FloatD_MRUV = float(D_MRUV)
                FloatA_MRUV = float(A_MRUV)
                FloatVi_MRUV = float(Vi_MRUV)
                FloatT_MRUV = math.sqrt(FloatD_MRUV / (FloatA_MRUV * 0.5))
                FloatVf_MRUV = (FloatD_MRUV / FloatT_MRUV) / 0.5 - FloatVi_MRUV
                print("El tiempo en el que transcurre el recorrido es:" + str(FloatT_MRUV) + "s")
                print("La velocidad final es: " + str(FloatVf_MRUV) + "m/s")
            elif D_MRUVinvalid + Vi_MRUVinvalid + Vf_MRUVinvalid == 0:
                FloatD_MRUV = float(D_MRUV)
                FloatVf_MRUV = float(Vf_MRUV)
                FloatVi_MRUV = float(Vi_MRUV)
                FloatT_MRUV = FloatD_MRUV / (0.5 * (FloatVf_MRUV + FloatVi_MRUV))
                FloatA_MRUV = ((FloatD_MRUV - FloatVi_MRUV * FloatT_MRUV) / (FloatT_MRUV ** 2)) / 0.5
                print("El tiempo en el que transcurre el recorrido es:" + str(FloatT_MRUV) + "s")
                print("La aceleracion es: " + str(FloatA_MRUV) + "m/s²")
            elif D_MRUVinvalid + Vf_MRUVinvalid + A_MRUVinvalid == 0:
                FloatD_MRUV = float(D_MRUV)
                FloatA_MRUV = float(A_MRUV)
                FloatVf_MRUV = float(Vf_MRUV)
                FloatVi_MRUV = math.sqrt(FloatVf_MRUV**2 / (2 * FloatA_MRUV * FloatD_MRUV))
                FloatT_MRUV = math.sqrt(FloatD_MRUV / (FloatA_MRUV * 0.5))
                print("La velocidad inicial es: " + str(FloatVi_MRUV) + "m/s")
                print("El tiempo en el que transcurre el recorrido es:" + str(FloatT_MRUV) + "s")
            elif D_MRUVinvalid + Vf_MRUVinvalid + T_MRUVinvalid == 0:
                FloatD_MRUV = float(D_MRUV)
                FloatT_MRUV = float(T_MRUV)
                FloatVf_MRUV = float(Vf_MRUV)
                FloatVi_MRUV = (FloatD_MRUV / FloatT_MRUV) / 0.5 - FloatVf_MRUV
                FloatA_MRUV = FloatD_MRUV / (0.5 * (FloatVf_MRUV + FloatVi_MRUV))
                print("La aceleracion es: " + str(FloatA_MRUV) + "m/s²")
                print("La velocidad inicial es: " + str(FloatVi_MRUV) + "m/s")
            elif D_MRUVinvalid + T_MRUVinvalid + A_MRUVinvalid == 0:
                FloatD_MRUV = float(D_MRUV)
                FloatT_MRUV = float(T_MRUV)
                FloatA_MRUV = float(A_MRUV)
                FloatVi_MRUV = (FloatD_MRUV -0.5 * FloatA_MRUV * FloatT_MRUV**2) / FloatT_MRUV
                FloatVf_MRUV = (FloatD_MRUV / FloatT_MRUV) / 0.5 - FloatVi_MRUV
                print("La velocidad inicial es: " + str(FloatVi_MRUV) + "m/s")
                print("La velocidad final es: " + str(FloatVf_MRUV) + "m/s")
            elif Vi_MRUVinvalid + Vf_MRUVinvalid + T_MRUVinvalid == 0:
                FloatT_MRUV = float(T_MRUV)
                FloatVf_MRUV = float(Vf_MRUV)
                FloatVi_MRUV = float(Vi_MRUV)
                FloatD_MRUV = 0.5 * (FloatVf_MRUV + FloatVi_MRUV) * FloatT_MRUV
                FloatA_MRUV = ((FloatD_MRUV - FloatVi_MRUV * FloatT_MRUV) / (FloatT_MRUV**2)) / 0.5
                print("La aceleracion es: " + str(FloatA_MRUV) + "m/s²")
                print("La distancia recorrida es: " + str(FloatD_MRUV) + "m")
            elif Vi_MRUVinvalid + A_MRUVinvalid + T_MRUVinvalid == 0:
                FloatA_MRUV = float(A_MRUV)
                FloatT_MRUV = float(T_MRUV)
                FloatVi_MRUV = float(Vi_MRUV)
                FloatD_MRUV = FloatVi_MRUV * FloatT_MRUV + 0.5 * FloatA_MRUV * FloatT_MRUV**2
                FloatVf_MRUV = (FloatD_MRUV / FloatT_MRUV) / 0.5 - FloatVi_MRUV
                print("La distancia recorrida es: " + str(FloatD_MRUV) + "m")
                print("La velocidad final es: " + str(FloatVf_MRUV) + "m/s")
            elif Vi_MRUVinvalid + Vf_MRUVinvalid + A_MRUVinvalid == 0:
                FloatA_MRUV = float(A_MRUV)
                FloatVf_MRUV = float(Vf_MRUV)
                FloatVi_MRUV = float(Vi_MRUV)
                FloatT_MRUV = (FloatVf_MRUV - FloatVi_MRUV) / FloatA_MRUV
                FloatD_MRUV = FloatVi_MRUV * FloatT_MRUV + 0.5 * FloatA_MRUV * FloatT_MRUV ** 2
                print("La distancia recorrida es: " + str(FloatD_MRUV) + "m")
                print("El tiempo en el que transcurre el recorrido es:" + str(FloatT_MRUV) + "s")
            elif Vf_MRUVinvalid + A_MRUVinvalid + T_MRUVinvalid == 0:
                FloatA_MRUV = float(A_MRUV)
                FloatT_MRUV = float(T_MRUV)
                FloatVf_MRUV = float(Vf_MRUV)
                FloatVi_MRUV = FloatVf_MRUV - FloatA_MRUV * FloatT_MRUV
                FloatD_MRUV = FloatVi_MRUV * FloatT_MRUV + 0.5 * FloatA_MRUV * FloatT_MRUV ** 2
                print("La distancia recorrida es: " + str(FloatD_MRUV) + "m")
                print("La velocidad inicial es: " + str(FloatVi_MRUV) + "m/s")

# Aca abajo estan si tiene 4 datos
        elif D_MRUVinvalid + T_MRUVinvalid + Vi_MRUVinvalid + Vf_MRUVinvalid + A_MRUVinvalid == 1:
            if D_MRUVinvalid + T_MRUVinvalid + Vi_MRUVinvalid + Vf_MRUVinvalid == 0:
                FloatD_MRUV = float(D_MRUV)
                FloatT_MRUV = float(T_MRUV)
                FloatVi_MRUV = float(Vi_MRUV)
                FloatVf_MRUV = float(Vf_MRUV)
                FloatA_MRUV = ((FloatD_MRUV - FloatVi_MRUV * FloatT_MRUV) / (FloatT_MRUV ** 2)) / 0.5
                print("La aceleracion es: " + str(FloatA_MRUV) + "m/s²")
            elif D_MRUVinvalid + T_MRUVinvalid + Vi_MRUVinvalid + A_MRUVinvalid == 0:
                FloatD_MRUV = float(D_MRUV)
                FloatT_MRUV = float(T_MRUV)
                FloatVi_MRUV = float(Vi_MRUV)
                FloatA_MRUV = float(A_MRUV)
                FloatVf_MRUV = (FloatD_MRUV / FloatT_MRUV) / 0.5 - FloatVi_MRUV
                print("La velocidad final es: " + str(FloatVf_MRUV) + "m/s")
            elif D_MRUVinvalid + T_MRUVinvalid + A_MRUVinvalid + Vf_MRUVinvalid == 0:
                FloatD_MRUV = float(D_MRUV)
                FloatT_MRUV = float(T_MRUV)
                FloatA_MRUV = float(A_MRUV)
                FloatVf_MRUV = float(Vf_MRUV)
                FloatVi_MRUV = FloatVf_MRUV - FloatA_MRUV * FloatT_MRUV
                print("La velocidad inicial es: " + str(FloatVi_MRUV) + "m/s")
            elif D_MRUVinvalid + A_MRUVinvalid + Vi_MRUVinvalid + Vf_MRUVinvalid == 0:
                FloatD_MRUV = float(D_MRUV)
                FloatA_MRUV = float(A_MRUV)
                FloatVi_MRUV = float(Vi_MRUV)
                FloatVf_MRUV = float(Vf_MRUV)
                FloatT_MRUV = math.sqrt(FloatD_MRUV / (FloatA_MRUV * 0.5))
                print("El tiempo en el que transcurre el recorrido es:" + str(FloatT_MRUV) + "s")
            elif T_MRUVinvalid + A_MRUVinvalid + Vi_MRUVinvalid + Vf_MRUVinvalid == 0:
                FloatA_MRUV = float(A_MRUV)
                FloatT_MRUV = float(T_MRUV)
                FloatVi_MRUV = float(Vi_MRUV)
                FloatVf_MRUV = float(Vf_MRUV)
                FloatD_MRUV = FloatVi_MRUV * FloatT_MRUV + 0.5 * FloatA_MRUV * FloatT_MRUV ** 2
                print("La distancia recorrida es: " + str(FloatD_MRUV) + "m")

    elif eleccion == 3:
        print("Perfecto, ha elegido MCL")
        print("Por favor, introduzca los datos de los que disponga, en caso de no tenerlos, pon -")
        print("La velocidad inicial y la posicion final siempre valdran 0 debido a las limitaciones del programa en su estado actual. Esto signica que solo se pueden hacer MCL donde se suelta a el cuerpo.")
        Vf_MCL = input("Velocidad final: ")
        T_MCL = input("Tiempo: ")
        Di_MCL = input("Posicion inicial: ")
        G = 9.8
        Vi_MCL = float(0)
        Df_MCL = float(0)

        if Vf_MCL == "-":
            Vf_MCLinvalid = 1
        else:
            Vf_MCLinvalid = 0
        if Di_MCL == "-":
            Di_MCLinvalid = 1
        else:
            Di_MCLinvalid = 0
        if T_MCL == "-":
            T_MCLinvalid = 1
        else:
            T_MCLinvalid = 0
        if Vf_MCL == 1 or Di_MCL == 1 and T_MCL == 1:
            print("No se han introducido datos suficentes")
        elif Di_MCLinvalid + Vf_MCLinvalid + T_MCLinvalid == 0:
            print("No ha introducido los datos correctamente")
        elif Vf_MCLinvalid == 1 or Di_MCLinvalid == 1 and T_MCLinvalid == 0:
            if Vf_MCLinvalid == 1 and Di_MCL == 1:
                Vf_MCL = float(Vi_MCL) - G * float(T_MCL)
                print("La velocidad antes de tocar el suelo es: " + str(-Vf_MCL) + "m/s")
                Di_MCL = float(Vi_MCL) * float(T_MCL) - 0.5*G * float(T_MCL)**2
                print("La altura inicial es: " + str(-Di_MCL) + "m")
            elif Di_MCLinvalid == 1:
                Di_MCL = float(Vi_MCL) * float(T_MCL) - 0.5*G * float(T_MCL)**2
                print("La altura inicial es: " + str(-Di_MCL) + "m")
            elif Vf_MCLinvalid == 1:
                Vf_MCL = float(Vi_MCL) - G * float(T_MCL)
                print("La velocidad antes de tocar el suelo es: " + str(-Vf_MCL) + "m/s")
        elif T_MCLinvalid == 1:
            T_MCL = (float(Vf_MCL) - float(Vi_MCL)) / - G
            print("El tiempo en el que transcurre el recorrido es: " + str(T_MCL) + "s")



    elif eleccion == 4:
        print("Finalizando programa...")
        menu = False
        break
