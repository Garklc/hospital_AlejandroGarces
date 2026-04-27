Hospital Trauma Team

Descripción del Proyecto

Este proyecto es una simulación básica de un sistema de atención hospitalaria, desarrollado en Python. El programa gestiona la asignación de boxes, la selección de instrumentos médicos según la enfermedad del paciente, la atención médica y la emisión de licencias médicas con posibles reembolsos. Está diseñado para demostrar conceptos fundamentales de programación como el uso de funciones, ciclos while y for, estructuras de datos (listas y diccionarios) y manejo básico de entrada/salida.

Características

•
Simulación de Sala de Espera: Simula el proceso de espera de pacientes con un sistema de turnos.

•
Asignación de Boxes: Busca y asigna boxes disponibles a los pacientes. Si no hay boxes, el paciente vuelve a la lista de espera.

•
Diagnóstico y Tratamiento: Identifica la enfermedad del paciente y sugiere el instrumento médico necesario para su tratamiento.

•
Atención Médica: Simula la atención del paciente, verificando la disponibilidad del instrumento médico.

•
Emisión de Licencias Médicas: Procesa la emisión de licencias, aplicando un reembolso de 100 unidades monetarias si la licencia es superior a 15 días.

•
Gestión de Saldo: Actualiza el saldo del paciente en función de la emisión de licencias.

•
Validación de Entrada: Incluye una función para validar que la entrada del usuario sea un número entero.

Cómo Ejecutar

Para ejecutar este programa, asegúrate de tener Python instalado en tu sistema. Luego, sigue estos pasos:

1.
Guarda el código proporcionado en un archivo llamado hospital.py.

2.
Abre una terminal o línea de comandos.

3.
Navega hasta el directorio donde guardaste el archivo hospital.py.

4.
Ejecuta el programa con el siguiente comando:

Bash


python hospital.py





5.
Sigue las instrucciones en pantalla para interactuar con la simulación del hospital.

Estructura del Código

El código está organizado en varias funciones para modularizar las diferentes etapas de la simulación:

•
obtener_mensaje(mensaje): Solicita una entrada numérica al usuario y la valida.

•
simular_espera(numero_atencion): Simula la sala de espera hasta que llega el turno del paciente.

•
buscar_box_disponible(lista_boxes): Encuentra y asigna un box disponible.

•
seleccionar_instrumentos(enfermedad, diccionario_instrumentos): Determina el instrumento necesario para una enfermedad.

•
atender_pacientes(instrumento_necesario, lista_de_doctor): Simula la atención médica y el tratamiento del paciente.

•
entregar_licencia(dias_licencia, saldo_actual): Gestiona la emisión de licencias y el reembolso.

Variables Globales

•
Saldo: Saldo inicial de cada paciente (20000).

•
paciente_sano: Booleano que indica si el paciente está sano.

•
licencia_entregada: Booleano que indica si la licencia ha sido entregada.

•
boxes: Lista de booleanos que representa la disponibilidad de los boxes (False = disponible, True = ocupado).

•
instrumentos_enfermedades: Diccionario que mapea enfermedades a los instrumentos/tratamientos necesarios.

•
doctor_con_indumentaria: Lista de instrumentos médicos que el doctor tiene a su disposición.

Autor

Alejandro Garces

Este proyecto fue desarrollado como parte de los fundamentos de programación.

