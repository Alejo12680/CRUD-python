import json

estudiantes = [
    {   
        "Documento": 1010,
        "Estudiante": "Alejandro Ramirez",
        "Nota-1": 4.5,
        "Nota-2": 3.4,
        "Nota-3": 2.6,
        "Promedio": 3.5
    },
    
    {   
        "Documento": 1111,
        "Estudiante": "Pilar Andrea Silva",
        "Nota-1": 3.5,
        "Nota-2": 4.4,
        "Nota-3": 5.0,
        "Promedio": 4.3
    }
]


with open("data.json", "w", encoding="utf-8") as file:
    json.dump(estudiantes, file, indent=4, ensure_ascii= False)
    print("Archivo Exportado Exitosamente")