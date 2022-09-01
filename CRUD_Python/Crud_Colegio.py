import json


def create():
    
    with open("data.json", "r", encoding="utf-8") as file:
        estudiantes = json.load(file)
        
        if len(estudiantes) == 0:
            print("\n El archivo esta vacio")
            
        else:
            print("********** Creación de Alumno **********")
            print("*"*40)
            codigo = int(input("Ingresa el DOCUMENTO del estudiante: "))
            nombre = input("Ingrese el NOMBRE del estudiante: ")
            nota1 = float(input("Ingrasa la NOTA periodo 1: "))
            nota2 = float(input("Ingrasa la NOTA periodo 2: "))
            nota3 = float(input("Ingrasa la NOTA periodo 3: "))
            promedio = round((nota1+nota2+nota3)/3, 1)

            studen = {
                "Documento": codigo,
                "Estudiante": nombre,
                "Nota-1": nota1,
                "Nota-2": nota2,
                "Nota-3": nota3,
                "Promedio": promedio
            }
            
            estudiantes.append(studen)
            
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(estudiantes, file, indent=4, ensure_ascii=False)
                
            print(f'Estudiante Ingresado Satisfactoriamente {studen} ')
    
    
def read():
    with open("data.json", "r", encoding="utf-8") as file:
        estudiantes = json.load(file)
        
        if len(estudiantes) == 0:
            print("\n El archivo esta vacio")
            
        else:
            print("********** Lista de Alumnos **********") 
            for values in estudiantes:
                print("*"*40)
                for key, value in values.items():
                    print(f'{key} : {value} ')
            

def update():
    with open("data.json", "r", encoding="utf-8") as file:
        estudiantes = json.load(file)
        
        if len(estudiantes) == 0:
            print("\n El archivo esta vacio")
            
        else:    
            print("********** Actualizar de Alumno **********")
            print("*"*40)
            
            codigo = int(input("Ingresa el documento del estudiante que desea modificar: "))
            
            #filtro:
            for item in range(0, len(estudiantes)):
                if estudiantes[item]["Documento"] == codigo:
                    print(estudiantes[item], "\n")
                    break

            flag = False
            for alumno in range(0, len(estudiantes)):
                if estudiantes[alumno]["Documento"] == codigo:
                    estudiantes.pop(alumno)
                    print("********** Reescribir Alumno **********")
                    print("*"*40)
                    codigo = int(input("Ingresa el DOCUMENTO del estudiante: "))
                    nombre = input("Ingrese el NOMBRE del estudiante: ")
                    nota1 = float(input("Ingrasa la NOTA periodo 1: "))
                    nota2 = float(input("Ingrasa la NOTA periodo 2: "))
                    nota3 = float(input("Ingrasa la NOTA periodo 3: "))
                    promedio = round((nota1+nota2+nota3)/3, 1)

                    nuevo = {
                        "Documento": codigo,
                        "Estudiante": nombre,
                        "Nota-1": nota1,
                        "Nota-2": nota2,
                        "Nota-3": nota3,
                        "Promedio": promedio
                    }
                    
                    estudiantes.append(nuevo)
                    flag =True
                    break
                
            if not flag:
                print("El Documento es Incorrecto")         

            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(estudiantes, file, indent=4) 
    
    
def delete():
    with open("data.json", "r", encoding="utf-8") as file:
        estudiantes = json.load(file)
        
        if len(estudiantes) == 0:
            print("\n El archivo esta vacio")
            
        else:    
            print("********** Eliminar de Alumno **********")
            print("*"*40)
            
            codigo = int(input("Ingresa el documento del estudiante que desea eliminar: "))
            
            #filtro:
            all_studen = [studen["Estudiante"] for studen in estudiantes if studen["Documento"] == codigo]
            
            for studen in all_studen:
                print(f'El estudiante {studen} a sido Eliminado')
                    
            #indice del json
            flag = False
            
            for alumno in range(0, len(estudiantes)):
                if estudiantes[alumno]["Documento"] == codigo:
                    estudiantes.pop(alumno)
                    flag =True
                    break
            if not flag:
                print("El Documento es Incorrecto")         

            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(estudiantes, file, indent=4)


def menu():
    while True:
        option = input("\n**** Menu Colegio ****\n (1)Crear Alumno.\n (2)Listar Alumnos.\n (3)Actualizar Alumnos.\n (4)Borrar Alumnos.\n (5)Salir del Programa\n Digita la Opcion: \n")
        
        if option == "1":
            create()
        
        if option == "2":
            read()
        
        if option == "3":
            update()
        
        if option == "4":
            delete()
        
        if option == "5":
            print("\n Gracias Por utilizar el Programa.")
            break
        
        seguir = input("\n Quieres hacer algo más [S] o [N]: ").upper()
        if seguir == "S":
            continue
        else:
            print("\n Gracias Por utilizar el Programa.")
            break




if __name__ == "__main__":
    menu()
