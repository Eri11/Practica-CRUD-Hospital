"""
author : Erika Eli Dominguez Carrillo
since 02-10-2021
"""

from pymongo import MongoClient
from bson import ObjectId
import random 
from random import sample, randint
from pprint import pprint


# Crea conexion con la base de datos
mongo_client = MongoClient(port=27017)

# Creacion / conexcion de la base de datos
db = mongo_client.starmedica

# Creacion/conexion con las colecciones
especialidades_collection = db.especialidades
hospitales_collection = db.hospitales
medicos_collection = db.medicos
pacientes_collection = db.pacientes



# Definicion de switch/case para entrar a cada collecion
#CREATE

def create_especialidad():
    #Declaracion de arreglo
    locs = ['AGS', 'CUU', 'CDJ', 'MER', 'MOR', 'QRT', 'SLP', 'VER']

    #Insercion de datos desde Python
    especialidades_collection.insert_many([
        {
        "depto" : "Ginecología y Obstetricia",
        "abbr" : "OBGYN",
        "loc" : [ locs[0], locs[1], locs[3] ] #Solo Algunos
        },
        {
            "depto" : "Pediatría",
            "abbr" : "PD",
            "loc" : locs #Todos
        },
        {
            "depto" : "Otorrinolaringología, Cirugia de Cabeza y Cuello",
            "abbr" : "ENT",
            "loc" : locs[randint(0, (len(locs) - 1))] #Uno al azar
        },
        {
            "depto" : "Gastroenterología",
            "abbr" : "GI",
            "loc" : random.sample(locs, randint(2, len(locs)-1)) #De aqui en delante lo dejaremos por de entre 2 a 8 locaciones al azar
        },
        {
            "depto" : "Hematología",
            "abbr" : "HEMA",
            "loc" : random.sample(locs, randint(2, len(locs)-1))
        },
        {
            "depto" : "Cirugia Oral y Maxilofacial",
            "abbr" : "MAXILO",
            "loc" : random.sample(locs, randint(2, len(locs)-1))
        },
        {
            "depto" : "Nefrología",
            "abbr" : "NEFRO",
            "loc" : random.sample(locs, randint(2, len(locs)-1))
        },
        {
            "depto" : "Psiquiatría",
            "abbr" : "PSYCH",
            "loc" : random.sample(locs, randint(2, len(locs)-1))
        },
        {
            "depto" : "Radiodiagnóstico",
            "abbr" : "RADIO",
            "loc" : random.sample(locs, randint(2, len(locs)-1))
        },
        {
            "depto" : "Transplante de Células Hematopoyéticas",
            "abbr" : "TCHP",
            "loc" : random.sample(locs, randint(2, len(locs)-1))
        },
        {
            "depto" : "Angiología, Cirugía Cardiovascular y Endovascular",
            "abbr" : "VASC-SURG",
            "loc" : random.sample(locs, randint(2, len(locs)-1))
        },
        {
            "depto" : "Traumatología y Ortopedia",
            "abbr" : "ORTHO",
            "loc" : random.sample(locs, randint(2, len(locs)-1))
        },
        {
            "depto" : "Cardiología Clínica",
            "abbr" : "CARDIO",
            "loc" : random.sample(locs, randint(2, len(locs)-1))
        },
        {
            "depto" : "Oncología Pediátrica",
            "abbr" : "PD-ONC",
            "loc" : random.sample(locs, randint(2, len(locs)-1))
        },
        {
            "depto" : "Nutrición",
            "abbr" : "NUTRI",
            "loc" : random.sample(locs, randint(2, len(locs)-1))
        }   
    ])

    print('Creacion de coleccion Especialidad creado correctamente')
    
def create_paciente():
    #Declaracion de arreglos
    first_names = ['Maria', 'Juan', 'Luis', 'David', 'Sofia', 'Jose', 'Francisco', 'Antonio', 'Edgar', 'Erika', 'Gabriel', 'Jesus', 'Miguel', 'Alejandro', 'Roberto', 'Pedro', 'Manuel', 'Margarita', 'Carmen', 'Jorge', 'Arely', 'Lucero', 'Flor', 'Evelyn', 'Mario']
    last_names = ['Gonzalez', 'Dominguez', 'Carrillo', 'Perez', 'Hernandez', 'Garcia', 'Lopez', 'Abreu', 'Acosta', 'Aguiar', 'Rosales', 'Reyna', 'Soto', 'Valverde', 'Fuentes', 'Ramirez', 'De la Rosa', 'Chico', 'Diaz', 'Medina', 'Molina', 'Ochoa', 'Ortega', 'Ortiz', 'Rios', 'Vasquez', 'Vazquez', 'Velasquez']
    
    tipos_calles = ['C.', 'Ave.', 'Blvd.']
    nombres_calles = ['Beethoven', 'Citadela' 'Kukulkan' 'Quetzalcoatl', 'Via Sicilia', 'De la Paloma','George Washington', 'M. Rocosas', 'Sierra Blanca', 'Mision de Satevo', '12a.', 'Melchor Ocampo', '4a', '10a', 'Sorgo', 'Zaragoza', 'Uva', 'Tapioca', 'Piña', 'De los Montes Urales', 'Fco. Baca', 'Belisario Dominguez', 'Cuauhtemoc', 'Plan de Ayala', 'Division del Norte', 'Fco. I. Madero']
    colonias = ['La Rinconada', 'Aguilas', 'Herradura La Salle', 'Residencial Universidad', 'Terrazas del Campestre', 'San Francisco Country Club', 'Club Campestre', 'Virreyes', 'Lomas de Guayangareo', 'Lomas del Santuario', 'Granjas', 'Las Arcadas', 'Mision de los Lagos', 'Campanario', 'Aeropuerto', 'Nuevo Juarez', 'Heroes de la Revolucion', 'Yucalpeten', 'San Damian', 'Xoclan la Reja', 'Paraiso Coatzacoalcos', 'Manuel Avila Camacho']
    ciudades = ['Chihuahua', 'Juarez', 'Delicias', 'Cuauhtemoc', 'Coatzacoalcos', 'Minatitlan', 'Catemaco', 'Merida', 'Morelia', 'Villa Madero', 'San Luis Potosi', 'Cardenas', 'El Naranjo']
    estados = ['AGS', 'CUU', 'CDJ', 'MER', 'MOR', 'QRT', 'SLP', 'VER']

    #Estructura ciclica
    for x in range(1, 1001):
        paciente = {
            'mrn' : random.randint(100000000, 599999999),
            'nombre' : {  "fn" : first_names[randint(0, (len(first_names) - 1))], "ln" : last_names[randint(0, (len(last_names) - 1))] + ' ' + last_names[randint(0, (len(last_names) - 1))] },
            'direccion' : { 
                "calle" :  tipos_calles[randint(0, (len(tipos_calles) - 1))]  + ' ' + nombres_calles[randint(0, (len(nombres_calles) - 1))], 
                "num" : random.randint(1000, 9999),
                "col" : colonias[randint(0, (len(colonias) - 1))],
                "ciudad" : ciudades[randint(0, (len(ciudades) - 1))],
                "estado" : estados[randint(0, (len(estados) - 1))],
                "cp" : random.randint(10001, 69999)
            },
            'dob' : { "dd": random.randint(1, 29), "mm" : random.randint(1, 12), "aaaa" : random.randint(1900, 2021) }
        }

        result = db.pacientes.insert_one(paciente)

        print('{0} Se ha creado exitosamente el registro del paciente {1}'.format(x, result.inserted_id))

    print('Directorio de pacientes creado exitosamente :)') 

def register_especialidad():
    print('Registro de Nueva Especialidad Medica')
    locs = ['AGS', 'CUU', 'CDJ', 'MER', 'MOR', 'QRT', 'SLP', 'VER']

    depto = input("Nombre del departamento: ")
    abbr = input("Abrev.: ").upper()

    especialidades_collection.insert_one({
        "depto" : depto,
        "abbr" : abbr,
        "loc" : random.sample(locs, randint(2, len(locs)-1)) #Por tiempo lo haremos aleatorio
    })

    print('Registro Exitoso')

def register_medico():
    print('Registro de Medicos')

    fn = input('Nombre: ')
    ln = input('Apellido(s): ')
    esp = input('Especialidad: ')
    hosp = input('Hospital: ')
    cons = input('No. de consultorio: ')
    tel = input('Telefono: ')
    cedProf = input('No. de Cedula Profesional: ')

    medicos_collection.insert_one({
        'nombre' : { 'fn' : fn, 'ln' : ln },
        'especialidad' : esp ,
        'hospital' : hosp ,
        'consultorio' : cons ,
        'telefono' : tel,
        'cedProf' : cedProf
    })

    print('Registro Exitoso')

#READ/RETRIEVE
def read_especialidad():
    especialidades_data_set = especialidades_collection.find({}, { '_id' : 0 })

    for especialidades_row in especialidades_data_set:
        pprint(especialidades_row,  indent = 3, width = 50)

def read_pacientes():
    pacientes_data_set = pacientes_collection.find({}, { 'mrn': 1, 'nombre' : 1, '_id' :0 })

    for pacientes_row in pacientes_data_set:
        pprint(pacientes_row,  indent = 3, width = 50) 

def read_hospital():
    hospitales_data_set = hospitales_collection.find()

    for hospitales_row in hospitales_data_set:
        pprint(hospitales_row)

def read_medicos():
    medicos_data_set = medicos_collection.find({}, { '_id' : 0 })

    for medicos_row in medicos_data_set:
        pprint(medicos_row, indent = 3, width =80)
            
#UPDATE
def update_pacientes():
    print('Actualiza la direccion del paciente')

    #Pregunta al usuario el MRN para buscar al paciente
    resp1 = int(input("Ingresa el MRN: "))
    
    calle = input("Nombre de calle: ")
    num = int(input("Num Externo: "))
    col = input("Colonia: ")
    ciudad = input("Ciudad: ")
    estado = input("Estado: ")
    cp = int(input("Codigo Postal: "))
    
    db.pacientes.find_one_and_update(
        { 'mrn' : resp1 },
        { '$set' : { 
            'direccion' : { 
                "calle" :  calle, 
                "num" : num,
                "col" : col,
                "ciudad" : ciudad,
                "estado" : estado,
                "cp" : cp
                }
            }
        }
    )

    print('Datos Actualizados Exitosamente')

#No funciono como queria...
def update_dir_medico():
    

    def update_site_cuu():
        medicos_collection.update(
            {'hospital' : 'ObjectId("6042a0cef7c5468e86d83fc6")'},
            { "$set" : { 'hospital' : "Star Medica Chihuahua" } }
        )

        print('Actualizacion Site CUU Finalizado')

    def update_site_ags():
        medicos_collection.update(
            {'hospital' : 'ObjectId("604299b5f7c5468e86d83fc5")'},
            { "$set" : { 'hospital' : "Star Medica Aguascalientes" } }
        )

        print('Actualizacion Site AGS Finalizado')

    
    print('Base de datos actualizada')    
                

def update_responsable_hosp():
    print('Actualizacion de Responsable Medico')
    op = int(input('¿Cual site?\n 1: AGS \n 2: CUU\n 3: CDJ\n 4: MER\n 5: MOR\n 6: QRT\n 7: SLP\n 8: VER\n'))
    resp = input('Nombre del responsable: ')

    site = [
        'Star Medica Aguascalientes',
        'Star Medica Chihuahua',
        'Star Medica Cd. Juarez',
        'Star Medica Merida',
        'Star Medica Morelia',
        'Star Medica Queretaro',
        'Star Medica San Luis Potosi',
        'Star Medica Veracruz'
    ]

    hospitales_collection.update_one(
            {'site' : site[op-1]},
            { "$set" : { 'responsable' : resp } }
    )

    print('Informacion actualizada exitosamente')

#DELETE

def delete_one_paciente():
    resp = input("Estas por eliminar un registro, ¿estas seguro de continuar? Y/N\n").upper()

    if (resp == 'Y'):
        mrn = int(input("No. Expediente Medico: "))
        pacientes_collection.delete_one(
            { 'mrn' : mrn }
        )
        print('Registro eliminado con exito')
    
    else:
        print('Nada ha sido modificado')

def delete_mult_registros():
    #Borrar los registros con numeracion menor a 5,000 
    print("Iniciando...")
    pacientes_collection.delete_many(
        { 'mrn' : { "$lte" : 200500000 } }
    )
    print("Registros Borrados exitosamente")


#Funcion Menu
def menu():
    while True:
        
        resp = int(input("\n¿A cuál collección deseas ingresar?\n\n 1: Especialidades médicas \n 2: Hospitales \n 3: Directorio Médico\n 4: Información de Pacientes\n\n"))
        
        if resp == 1 :
            print("Especialidades\n")
            #CR
            op = int(input("Elige la opcion deseada:\n 1: Mostrar directorio de especialidades\n 2: Registrar especialidad\n\n"))
            if op == 1:
                read_especialidad()
                menu()
                break

            elif op == 2:
                register_especialidad()
                menu()
                break

            else:
                print("Opcion no valida. Adios")
                menu()
            break
        
        elif resp == 2:
            print("Hospitales\n")
            #RU
            op = int(input("Elige la opcion deseada:\n 1: Mostrar directorio de hospitales\n 2: Actualizar responsable\n\n"))
            if op == 1:
                read_hospital()
                menu()
                break

            elif op == 2:
                update_responsable_hosp()
                menu()
                break

            else:
                print("Opcion no valida. Adios")
                menu()
            break


        elif resp == 3:
            print("Directorio Medico\n")
            #CR
            op = int(input("Elige la opcion deseada:\n 1: Mostrar directorio medico\n 2: Registrar nuevo medico\n\n"))
            if op == 1:
                read_medicos()
                menu()
                break

            elif op == 2:
                register_medico()
                menu()
                break

            else:
                print("Opcion no valida. Adios")
                menu()
            break

        elif resp == 4 :
            print("Información de Pacientes\n")
            #RUD
            op = int(input("Elige la opcion deseada:\n 1: Mostrar listado de pacientes\n 2: Actualizacion de direccion\n 3: Borrar registro\n\n"))
            if op == 1:
                read_pacientes()
                menu()
                break

            elif op == 2:
                update_pacientes()
                menu()
                break

            elif op == 3:
                delete_one_paciente()
                menu()
                break

            else:
                print("Opcion no valida. Adios")
                menu()
            break


        else:
            print("Opcion no valida. Intenta nuevamente")
            menu()

print("BIENVENIDO A LA BASE DE DATOS DE STARMEDICA")

menu()

#create_especialidad()
#read_especialidad()
#read_hospital()
#read_medicos()
#create_paciente()
#read_pacientes()
#update_pacientes()
#register_especialidad()
#update_dir_medico()
#update_responsable_hosp()
#delete_one_paciente()
#delete_mult_registros()