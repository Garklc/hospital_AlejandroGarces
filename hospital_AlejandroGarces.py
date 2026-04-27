# Nombre: Alejandro Garces
# Fundamentos de programacion
# hospital.py

Saldo= 20000    # saldo inicial de cada paciente, al iniciar el programa
paciente_sano= False    # variable booleana para saber si el paciente esta sano
licencia_entregada= False   # variable booleana para saber si la licencia fue entregada

boxes= [True, False, False, False, False]  # boxes disponibles: false= disponible, true= ocupado

instrumentos_enfermedades= {    # instrumentos medicos y tratamientos correspondientes

    "resfrio": "paracetamol 500mg",     # paracetamol 500mg para tratar resfrio
    "fractura":"yeso",                 # yeso para tratar fractura
    "migraña":"migranol",               # migranol para tratar migraña
    "corte":"sutura",                   # sutura para tratar corte
    "fiebre":"ibuprofeno"               # ibuprofeno para tratar fiebre
}

doctor_con_indumentaria=["paracetamol 500mg", "yeso", "migranol", "sutura", "ibuprofeno"] # lista de instrumentos medicos con indumentaria

#funcion para obtener un numero entero, se repite hasta que se ingrese un numero
#busque la isdigit para saber si lo que se ingreso es un numero
#se pudo realizar con un validacion de errores usando try except pero lo veremos la proxima clase

def obtener_mensaje(mensaje): 

    while True: #usamos el ciclo while para que se repita hasta que se ingrese un numero infinitamente 
        entrada= input(mensaje)
        if entrada.isdigit(): #se usa while y isdigit para no romper el sistema
            return int(entrada)
        else:
            print("\nError, ingrese un numero valido")


def simular_espera(numero_atencion): # se usa una funcion para simular el tiempo de espera del paciente
    print("\nSala de espera hospital 'Trauma Team'") # se imprime la sala de espera en pantalla

    turno_actual=1 # se define una variable para el turno actual
    while turno_actual<numero_atencion: # se usa un ciclo while mientras llega el turno del paciente, se usa while para repetir el ciclo
        print(f"atendiendo a turno: {turno_actual}") # se imprime el turno actual en pantalla
        turno_actual+=1 # se aumenta el turno actual en +1

    print(f"Turno {numero_atencion} esta siendo atendido") # se imprime el turno el cual sera atendido


def buscar_box_disponible(lista_boxes): # se usa una funcion para buscar un box disponible
    print("\nBuscar box disponible") # se imprime la sala box disponible en pantalla
    for i in range(len(lista_boxes)): # se usa un ciclo for para recorrer la lista

        if lista_boxes[i]== False: # se usa un if para desicion y saber si el box esta disponible
            lista_boxes[i]= True # se cambia el estado del box a ocupado
            print(f"Box {i+1} asignado") # se imprime el box disponible y es asignado
            return i+1 # retorna el box asignado

    print("No hay boxes disponibles") # se imprime que no hay boxes disponibles
    return None # retorna None si esque no se encuentra box disponible

def seleccionar_instrumentos(enfermedad, diccionario_instrumentos): # se usa una funcion para seleccionar los instrumentos medicos
    print("\nselecion de instrumentos medicos: ") # se imprime la seleccion de instrumentos medicos

    if enfermedad in diccionario_instrumentos: # se usa un if para saber si la enfermedad esta en el diccionario
       instrumento= diccionario_instrumentos[enfermedad] # se asigna el instrumento a la enfermedad dada
       print(f"usted esta en el box por '{enfermedad}'") # se imprime la enfermedad
       print(f"su atencion requiere el uso de '{instrumento}' para su pronta recuperacion") #se imprime el instrumento señalado
       return instrumento # se retorna el instrumento 
    else: # se usa si no se encuentra la enfermedad
        print("enfermedad no detectada") # se imprime que no se encuentra la enfermedad
        return None # se retorna None
    

def atender_pacientes(instrumento_necesario, lista_de_doctor): # se usa una funcion para atender al paciente
    print("\nAtencion medica") # se imprime la atencion medica
    if instrumento_necesario != None: # se usa un if para saber si el existe el instrumento
        if instrumento_necesario in lista_de_doctor: # se usa un if para saber si el instrumento esta en la lista
            print(f"el medico utiliza : {instrumento_necesario}") # se imprime el instrumento usado
            print("el paciente fue tratado y esta sano") # se imprime que el paciente fue tratado con exito
            return True # se retorna True ya que el paciente fue tratado con exito
        else: 
            print(f" el medico no encuentra el instrumento {instrumento_necesario}") # se imprime que no se encuentra el instrumento    
            return False # se retorna False ya que el paciente no fue tratado
    else: # se usa si no se encuentra el instrumento
         print("no se puede atender al paciente") # se imprime que no se puede atender al paciente
         return False # se retorna False
        
def entregar_licencia(dias_licencia, saldo_actual): # se usa una funcion para entregar la licencia
    print("\nentrega de licencia medica") # se imprime la entrega de la licencia en pantalla
    print(f"dias de licencia: {dias_licencia}") # se imprime los dias de licencia en pantalla
    
    if dias_licencia > 15: # se usa un if para saber si la licencia es mayor a 15 dias
        saldo_actual+= 100 # se aumenta el saldo actual en +100 como dice el enunciado
        print("licencia entregada y es mayor a 15 dias") # se imprime que la licencia fue entregada
        print(f"se entrego reembolso de 100 ") # se imprime el reembolso entregado
    else: # se usa si la licencia es menor a 15 dias
        print("licencia menor a 15 dias") # se imprime que la licencia es menor a 15 dias
        print("no se entregara reembolso") # se imprime que no se entregara reembolso como dice el enunciado
    
    print(f"\nsaldo actual: {saldo_actual}") # se imprime el saldo final
    return saldo_actual # se retorna el saldo corregido 


print("==========================================") # se imprime el encabezado una linea linda
print("Bienvenido al Hospital Trauma Team") # se imprime el encabezado
print("==========================================") # se imprime el encabezado una linea linda


while paciente_sano== False or licencia_entregada== False: # se usa un ciclo while para repetir el ciclo

    print("\n--- nuevo intento de atencion ---") # se imprime el encabezado po pantalla

    numero= obtener_mensaje("\nIngrese el numero de atencion: ") # se obtiene el numero de atencion usando la funcion 
    simular_espera(numero) # se simula la espera del paciente usando la funcion
    box= buscar_box_disponible(boxes) # se llama a la funcion buscando el box libre

    if box != None: # se usa un if para saber si hay boxes disponibles
        print("\natenciones registradas: ") # se muestran los tratamientos que puedes acceder
        print("resfrio")
        print("fractura")
        print("migraña")
        print("corte")
        print("fiebre")

        #se usa .lower para que se ingrese el tratamiento este en minusculas siempre
        #asi validamos que la opcion este los tratmientos y no tenga errores de escritura y/o mayusculas
        enfermedad_registrada= input("\nIngrese la atencion registrada: ").lower()
        #busca el instrumento en el diccionario
        instrumento_necesario= seleccionar_instrumentos(enfermedad_registrada, instrumentos_enfermedades)
        # se atiende al paciente usando la funcion
        paciente_sano= atender_pacientes(instrumento_necesario, doctor_con_indumentaria)

        if paciente_sano==True: # se usa un if para saber si el paciente esta sano y seguir con la licencia
            dias= obtener_mensaje("\nIngrese los dias de licencia: ") # se piden los dias de licencia
            Saldo= entregar_licencia(dias, Saldo) # se entrega la licencia y se actualiza el saldo dependiendo de los dias
            licencia_entregada= True # se cambia el valor de la variable licencia
        else: # si no esta sano paciente es False y se repite por el ciclo while
            print("\nno se puede atender al paciente. volvera a lista de espera") # se imprime que no se puede atender al paciente
        
        # esta parte es muy importante ya que libera el box y lo cambia a disponible
        #en un futuro se puede volver a usar el mismo box ya que estara disponible de nuevo
        boxes[box-1]= False # libera el box
    else: 
        # si no hay box disponible las variables son False y se repite el ciclo por el while
        print("\nno hay boxes disponibles. volvera a lista de espera")
# se termina el ciclo el paciente esta sano y con licencia
print("==========================================")  # linea decorativa
print("\nFin del programa") # se imprime el fin del programa
print("\nel paciente esta sano y con licencia medica") # se imprime el fin del programa
print("==========================================") # linea decorativa