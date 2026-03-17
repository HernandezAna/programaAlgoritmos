if __name__ == "__main__":
    from holaMundo import Mensaje
    from operacionesMatematicas import OperacionesMatematicas

    print("Este es el programa principal")
    print("selecciona la opcion que deseas ejecutar:")
    print("1. Hola Mundo")
    print("2. Operaciones Matematicas") 
    print("3.- Calcular la edad de una persona")
    opcion = int(input("Ingrese el número de la opción: "))

    if opcion == 1:
        mensaje = Mensaje("Hola Mundo desde el programa principal")
        mensaje.mostrar()
    elif opcion == 2:
        operaciones = OperacionesMatematicas()
        a=int(input("Ingrese el primer número: "))
        b=int(input("Ingrese el segundo número: "))
        
        print("Suma:", operaciones.sumar(a, b))
        print("Resta:", operaciones.restar(a, b))
        print("Multiplicación:", operaciones.multiplicar(a, b))
        print("División:", operaciones.dividir(a, b))
    elif opcion == 3:        
        from persona import Persona
        nombre = input("Ingrese el nombre de la persona: ")
        anio_nacimiento = int(input("Ingrese el año de nacimiento: "))
        persona = Persona(nombre, anio_nacimiento, 0)
        edad = persona.calcular_edad(2026)
        print(f"{persona.nombre} tiene {edad} años.")
    else:
        print("Opción no válida")