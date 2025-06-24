from os import system
from time import sleep

usuarios = {}





while True:

  system("cls")
  print("MENU PRINCIPAL")
  print("1. Registrar nuevo usuario")
  print("2. Consultar usuario existente")
  print("3. Eliminar un usuario")
  print("4. Finalizar programa")

  opcion = input("Seleccione una opción: ").strip()

  if opcion == "1":

    while True:
      nombre = input("Nombre de usuario: ").strip()
      if nombre in usuarios:
        print("¡Ese nombre ya está registrado! Prueba con otro.")
      else:

        break



    while True:

      sexo = input("Sexo (M o F): ").strip().upper()

      if sexo not in ["M", "F"]:

        print("Entrada no válida. Solo se permite 'M' o 'F'.")
      else:
        break

    while True:
      contraseña = input("Cree una contraseña: ").strip()
      if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
    
      if " " in contraseña:
      print("No se permiten espacios en la contraseña.")

      if not () for  in contraseña):
        print("Debe contener al menos una letra.")
    
      if not (c.isdigit() for c in contraseña):
        print("Debe contener al menos un número.")
      print("Contraseña aceptada.")
      usuarios[nombre] = {"sexo": sexo, "contraseña": contraseña}
      print("¡Usuario registrado correctamente!")
      break


    sleep(2)

  elif opcion == "2":
    nombre = input("Ingrese el nombre del usuario a buscar: ").strip()
    if nombre in usuarios:
      datos = usuarios[nombre]
      print(f"Sexo: {datos['sexo']}")
      print(f"Contraseña: {datos['contraseña']}")
    else:
      print("Usuario no encontrado en la base de datos.")
    sleep(2)

  elif opcion == "3":
    nombre = input("Indique el nombre del usuario a eliminar: ").strip()
    if nombre in usuarios:

      del usuarios[nombre]

      print("Eliminación completada con éxito.")
    else:

      print("No fue posible eliminar. Usuario inexistente.")
    sleep(2)

  elif opcion == "4":
    print("Cerrando el sistema... ¡Hasta pronto!")
    sleep(1.5)
    break

  else:
    print("Opción no reconocida. Elija una del 1 al 4.")
    sleep(1.5)

 