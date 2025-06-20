from fastapi import FastAPI
from typing import Dict, List, Optional
from pydantic import BaseModel


class User(BaseModel):
    Nombre: str
    Matricula: str
    Edad: int
    Carrera: str
    Genero: str
    Deporte: str
    Pelicula: str
    Hobby: str
    Color: str
    Musica: str
    Facultad: str


app = FastAPI()

alumnos = [
    User(Nombre="Emmanuel Ricardo Pérez Vázquez", Matricula="202277113", Edad=24, Carrera="Ingeniería en Ciencias de la Computación", Genero="Masculino",
         Deporte="baseball", Pelicula="klaus", Hobby="jugar bideu", Color="verde", Musica="rock", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Jovany Solis Ortiz", Matricula="202268439", Edad=23, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino", Deporte="Natación",
         Pelicula="500 days with summer", Hobby="Gym, escribir", Color="verde", Musica="Rap, Pop, Rock indie", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Efrain Adolfo García Castañeda", Matricula="202036939", Edad=25, Carrera="Ingeniería en Ciencias de la Computación", Genero="Masculino", Deporte="Básquet",
         Pelicula="Como entrenar a tu dragón", Hobby="Jugar videojuegos y escuchar música", Color="Rosa Mexicano", Musica="Pop", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Maximiliano Aranda León", Matricula="202213246", Edad=21, Carrera="Ingenieria en tecnologías de la información", Genero="Masculino",
         Deporte="Tennis", Pelicula="Mad Max: Fury Road", Hobby="Dibujar", Color="Blanco", Musica="Rock", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Miguel Angel Castillo Corona", Matricula="202221447", Edad=21, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino", Deporte="Fútbol",
         Pelicula="Atrapame si puedes", Hobby="Escuchar música", Color="Rosa", Musica="Baladas en español", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Jared Ubaldo Sanchez Lopez", Matricula="202253100", Edad=22, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino",
         Deporte="Básquetbol", Pelicula="Spiderman 2", Hobby="Videojuegos", Color="Azul", Musica="Rock", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Mario Alberto Navarro Soto", Matricula="202264602", Edad=21, Carrera="Ingeniería en Ciencias de la Computación", Genero="Masculino",
         Deporte="Boxeo", Pelicula="Chronicle", Hobby="Videojuegos", Color="Verde", Musica="Clásica", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Javier Mendieta Pérez", Matricula="202263837", Edad=21, Carrera="Ingeniería en Ciencias de la Computación", Genero="Masculino",
         Deporte="Atletismo", Pelicula="Pacific Rim", Hobby="Videojuegos", Color="Verde", Musica="Rock/Pop", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Jorge Damian Cocone", Matricula="202221609", Edad=22, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino", Deporte="Ciclismo",
         Pelicula="Volver al futuro", Hobby="Ilustracion digital", Color="Rosa pastel", Musica="Punk", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Montserrat Oidor Trujillo", Matricula="202349207", Edad=23, Carrera="Licenciatura en Ciencias de la Computación", Genero="Femenino",
         Deporte="natación", Pelicula="Ratatouille", Hobby="salir a caminar", Color="cian", Musica="pop", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Elías Romero Morales", Matricula="202157519", Edad=21, Carrera="Ingeniería en Ciencias de la Computación", Genero="Masculino",
         Deporte="Box", Pelicula="Batman the dark knight", Hobby="Dibujar", Color="Azul", Musica="Rock", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Alfredo Ramírez Candia", Matricula="202375947", Edad=19, Carrera="Ingeniería en Ciencias de la Computación", Genero="Masculino", Deporte="Fútbol",
         Pelicula="El padrino ll", Hobby="Tocar la guitarra", Color="Verde", Musica="Rock progresivo", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Victor Alexander Rodriguez Cuahuizo", Matricula="202353593", Edad=19, Carrera="Licenciatura en Ciencias de la Computación", Genero="Masculino",
         Deporte="Tiro con arco", Pelicula="The sadness", Hobby="Leer", Color="Cyan", Musica="Trap arg", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Rocío Ramírez Fabián", Matricula="202153429", Edad=22, Carrera="Ingeniería en Tecnologías de la Información", Genero="Femenino",
         Deporte="Atletismo", Pelicula="A 2 metros de ti", Hobby="Ir al gym", Color="Negro", Musica="Pop", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Manuel Ramos Varela", Matricula="202352613", Edad=23, Carrera="Licenciatura en Ciencias de la Computación", Genero="Masculino",
         Deporte="Ciclismo", Pelicula="Top Gun 2", Hobby="Jugar videojuegos", Color="Rojo", Musica="Rock", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Angel Martinez Hernández", Matricula="202338817", Edad=21, Carrera="Licenciatura en Ciencias de la Computación", Genero="Masculino", Deporte="Ciclismo recreativo",
         Pelicula="Interestelar", Hobby="Pasar el día en la bici, o jugando videojuegos", Color="Turquesa", Musica="Rock en español y Cumbias", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Rivaldo Mendez Carranza", Matricula="202233629", Edad=26, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino",
         Deporte="Futbol", Pelicula="Up", Hobby="Ir al gym", Color="Negro", Musica="Corridos Tumbados", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Guadalupe Tovar Cruz", Matricula="202163318", Edad=26, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino",
         Deporte="Béisbol", Pelicula="The Grand Budapest Hotel", Hobby="Escribir", Color="Verde", Musica="Pop", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Erick Cruz Cortes", Matricula="201907093", Edad=24, Carrera="Ingeniería en Ciencias de la Computación", Genero="Masculino", Deporte="Voleibol",
         Pelicula="Rápidos y furiosos", Hobby="Jugar voleibol", Color="Negro", Musica="Norteño", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Erwin Gael Avendaño Vega", Matricula="202220926", Edad=20, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino",
         Deporte="Baloncesto", Pelicula="Al filo del mañana", Hobby="Jugar videojuegos", Color="Verde", Musica="Pop", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Abrahan lopez Vázquez", Matricula="202228423", Edad=27, Carrera="Ingeniería en Ciencias de la Computación", Genero="Masculino",
         Deporte="Básquetbol", Pelicula="Volver al futuro", Hobby="Acampar", Color="Cafe", Musica="Metal", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Angel Sarmiento Totolhua", Matricula="202253882", Edad=21, Carrera="Ingeniería en Tecnologías de la Información",
         Genero="Masculino", Deporte="futbol", Pelicula="", Hobby="gym", Color="negro", Musica="", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Gabriela Pérez Arce", Matricula="202265304", Edad=21, Carrera="Ingeniería en Ciencias de la Computación", Genero="Femenino",
         Deporte="Natación", Pelicula="Turning red", Hobby="Dibujar", Color="Cian", Musica="Pop-rap", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Juan Gutierrez Díaz", Matricula="202166332", Edad=22, Carrera="Ingeniería en Ciencias de la Computación", Genero="Masculino", Deporte="MMA",
         Pelicula="Sangre por Sangre", Hobby="Bataca, gym, ajedrez", Color="Negro", Musica="Rock", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Omar Márquez Garcia", Matricula="", Edad=26, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino", Deporte="Futbol",
         Pelicula="", Hobby="Jugar videojuegos", Color="Negro y Dorado", Musica="Musica de los 80's", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Regina Monserrat Avelino Farfán", Matricula="", Edad=22, Carrera="Ingeniería en Tecnologías de la Información", Genero="Femenino",
         Deporte="Patinaje en línea", Pelicula="Shrek", Hobby="Taekwondo", Color="Azul", Musica="Pop", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Victor Angel Peralta Fuentes", Matricula="202350319", Edad=24, Carrera="Licenciatura en Ciencias de la Computación", Genero="Masculino",
         Deporte="Basquet", Pelicula="La cosa", Hobby="Jugar videojuegos", Color="Verde", Musica="Rock", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Jonathan Gabriel Garcia Castillo", Matricula="202273834", Edad=22, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino",
         Deporte="Atletismo", Pelicula="Interstellar", Hobby="Escribir", Color="Azul", Musica="Alternativo", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Diego Alexis López Pérez", Matricula="202262883", Edad=21, Carrera="Licenciatura en Ciencias de la Computación", Genero="Masculino",
         Deporte="Ping pong", Pelicula="Sherk 2", Hobby="Jugar Ajedrez", Color="Morado", Musica="Banda", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Ever Zuriel López Ramírez", Matricula="202228369", Edad=21, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino",
         Deporte="Basquetbol", Pelicula="Ready Player One", Hobby="Jugar videojuegos", Color="Negro", Musica="Breakcore", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Ángel Ignacio De La Llave Mendez", Matricula="202230031", Edad=20, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino",
         Deporte="Natacion", Pelicula="Selena The movie", Hobby="Guitarra", Color="Menta", Musica="Rock", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Jorge Rojas Ruiz", Matricula="202251246", Edad=21, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino",
         Deporte="Voleibol", Pelicula="Deadpool", Hobby="Gym", Color="Azul", Musica="Bolero", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Alexandro González Sánchez", Matricula="202226780", Edad=21, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino",
         Deporte="Ciclismo", Pelicula="Interstela 5555", Hobby="Dibujar", Color="Rojo", Musica="Indie", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Brayan Blancas Monsalvo", Matricula="201965973", Edad=23, Carrera="Ingeniería en Ciencias de la Computación", Genero="Masculino",
         Deporte="atletismo", Pelicula="pacific rim", Hobby="jugar vídeojuegos", Color="morado", Musica="nu metal", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Ignacio", Matricula="202222543", Edad=22, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino", Deporte="Futbol americano",
         Pelicula="Dune 2", Hobby="Dibujar", Color="Rosa", Musica="Regional mexicana", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Joselyn Ramírez Lima", Matricula="202248964", Edad=21, Carrera="Ingeniería en Tecnologías de la Información", Genero="Femenino",
         Deporte="Basketball", Pelicula="La Propuesta", Hobby="Scrapbook", Color="Rosa", Musica="Pop", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Moisés Machorro Portilla", Matricula="202232944", Edad=21, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino", Deporte="Basketball",
         Pelicula="Amigos intocables", Hobby="Hacer música r&b y variantes", Color="Verde oscuro", Musica="Soul", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Arantza Aili Tenorio Domínguez", Matricula="202254883", Edad=21, Carrera="Ingeniería en Tecnologías de la Información", Genero="Femenino",
         Deporte="voley", Pelicula="Juego de gemelas", Hobby="tomar fotos", Color="azul", Musica="Pop", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Ana Karen Mani Márquez", Matricula="202044959", Edad=23, Carrera="Arquitectura", Genero="Femenino", Deporte="Básquet",
         Pelicula="El cadáver de la novia", Hobby="Dibujar", Color="Azul", Musica="Pop", Facultad="Facultad de Arquitectura"),
    User(Nombre="Saul Itzcoatl Tototzintle", Matricula="292431194", Edad=19, Carrera="Contaduría Publica", Genero="Masculino", Deporte="Basquetbol",
         Pelicula="Como entrenar a tu dragon", Hobby="Jugar videojuegos", Color="Verde", Musica="Electrónica", Facultad="Facultad de Contaduría Pública"),
    User(Nombre="Andrea Margarita Maldonado Morales", Matricula="202233003", Edad=23, Carrera="Ingeniería en Tecnologías de la Información", Genero="Femenino",
         Deporte="Futbol", Pelicula="Como perder a un hombre en 10 días", Hobby="Pintar", Color="Verde", Musica="Pop", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Alicia Gutierrez Jiménez", Matricula="202039510", Edad=23, Carrera="Arquitectura", Genero="Femenino", Deporte="Básquet",
         Pelicula="Memorias de un caracol", Hobby="Cuidar plantas", Color="Blanco y azul", Musica="Todas", Facultad="Facultad de Arquitectura"),
    User(Nombre="José Antonio Daniel", Matricula="202238037", Edad=20, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino", Deporte="Bádminton",
         Pelicula="Lalaland", Hobby="Ver videos", Color="Azul marino", Musica="Universal stereo", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Jared Cervantes Rodriguez", Matricula="202229672", Edad=21, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino",
         Deporte="Ninguno", Pelicula="Frozen", Hobby="Aprender idiomas", Color="Verde", Musica="R&B", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Guillermo Solis Cuautle", Matricula="202091881", Edad=26, Carrera="Arquitectura", Genero="Masculino", Deporte="Atletismo",
         Pelicula="Maze runner", Hobby="Ver series , películas, escuchar música", Color="Azul", Musica="Pop", Facultad="Facultad de Arquitectura"),
    User(Nombre="Angel Kenai Sanchez Rojas", Matricula="202253339", Edad=20, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino",
         Deporte="Basketball", Pelicula="Parásitos", Hobby="Hacer Ejercicio", Color="Morado", Musica="Ritmos latinos", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Ricardo Alonso Vara Castañeda .", Matricula="202164145", Edad=21, Carrera="Ingeniería en Tecnologías de la Información.", Genero="Masculino",
         Deporte="Atletismo.", Pelicula="Acción.", Hobby="Hacer ejercicio.", Color="Rojo o Azul.", Musica="Regional Mexicano.", Facultad="Facultad de Ciencias de la Computación."),
    User(Nombre="Luis Roberto Telles Coyopol", Matricula="202162115", Edad=22, Carrera="Arquitectura", Genero="Masculino", Deporte="Futbol Asociación (Fútbol)", Pelicula="Hachiko",
         Hobby="Ver contenido de Streaming/ Reproducción de videos", Color="Morado", Musica="Dance Pop/ Electro Pop en Inglés", Facultad="Facultad de Arquitectura"),
    User(Nombre="Geovanni Cerón Reyes", Matricula="202320421", Edad=20, Carrera="Ingeniería en Ciencias de la Computación", Genero="Masculino",
         Deporte="Basquetbol", Pelicula="Interestelar", Hobby="Gym", Color="Azul", Musica="Pop en español", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Luis Angel Reyes Campechano", Matricula="202154742", Edad=22, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino",
         Deporte="Fútbol/soccer", Pelicula="Interestelar", Hobby="Tocar guitarra", Color="Negro", Musica="Rock", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Samuel Zaid Cruz Ramirez", Matricula="202229917", Edad=20, Carrera="Ingeniería en Ciencias de la Computación", Genero="Masculino",
         Deporte="Natacion", Pelicula="Titanes del Pacifico", Hobby="Hacer ejercicio", Color="Rojo", Musica="Rock", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Marco Antonio Hernández Santiesteban", Matricula="202123954", Edad=22, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino", Deporte="Básquet",
         Pelicula="Así en la tierra como en el infierno", Hobby="Dibujar", Color="Negro", Musica="Regional mexicano", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Jhoel Boset Hernández Hernández", Matricula="202240624", Edad=26, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino",
         Deporte="Fútbol", Pelicula="El Padrino", Hobby="Pasar tiempo con la familia", Color="Verde", Musica="Rap", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Pablo Eduardo Rojas Martínez", Matricula="202156865", Edad=22, Carrera="Medicina", Genero="Masculino", Deporte="volleyball",
         Pelicula="Intensamente", Hobby="Jugar vidojuegos", Color="verde", Musica="pop en ingles", Facultad="Facultad de Medicina"),
    User(Nombre="Nancy Paola Martínez Tobón", Matricula="202233429", Edad=21, Carrera="Ingeniería en Tecnologías de la Información", Genero="Femenino", Deporte="Correr",
         Pelicula="El espanta tiburones", Hobby="Preparar bocadillos", Color="Gris y beige", Musica="Reggae", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Raquel Garzón Soto", Matricula="202239618", Edad=21, Carrera="Ingeniería en Tecnologías de la Información", Genero="Femenino", Deporte="Voleibol",
         Pelicula="A dos metros de ti", Hobby="Escuchar música", Color="Lila y vino", Musica="Jazz", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Alfredo Escudero Rivera", Matricula="202222184", Edad=21, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino",
         Deporte="Fútbol", Pelicula="Spider-Man (2002)", Hobby="Tocar la guitarra", Color="Negro", Musica="R&B/Pop", Facultad="Facultad de Ciencias de la Computación"),
    User(Nombre="Antonio Morales Badillo", Matricula="202139052", Edad=21, Carrera="Ingeniería en Tecnologías de la Información", Genero="Masculino", Deporte="Basquetbol",
         Pelicula="Iron Man: el hombre de hierro", Hobby="Videojuegos", Color="Cyan", Musica="Vocaloid", Facultad="Facultad de Ciencias de la Computación")
]

######################################################

# GET por Carrera y Género


@app.get("/alumnos/carrera/{carrera}/genero/{genero}")
async def get_alumnos_por_carrera_y_genero(carrera: str, genero: str):
    alumnos_filtrados = filter(
        lambda alumno: (carrera.lower() in alumno.Carrera.lower()) and
        (alumno.Genero.lower() == genero.lower()),
        alumnos
    )
    return list(alumnos_filtrados)

# GET por Facultad y Deporte


@app.get("/alumnos/facultad/{facultad}/deporte/{deporte}")
async def get_alumnos_por_facultad_y_deporte(facultad: str, deporte: str):
    alumnos_filtrados = filter(
        lambda alumno: (facultad.lower() in alumno.Facultad.lower()) and
        (deporte.lower() in alumno.Deporte.lower()),
        alumnos
    )
    return list(alumnos_filtrados)


# GET por Matrícula
@app.get("/alumnos/matricula/{matricula}")
async def get_alumno_por_matricula(matricula: str):
    alumnos_filtrados = filter(
        lambda alumno: alumno.Matricula == matricula, alumnos)
    try:
        return list(alumnos_filtrados)[0]
    except:
        return {"error": "No se ha encontrado el alumno con esa matrícula"}

# GET por Nombre (búsqueda exacta)


@app.get("/alumnos/nombre/{nombre}")
async def get_alumno_por_nombre(nombre: str):
    alumnos_filtrados = filter(
        lambda alumno: alumno.Nombre.lower() == nombre.lower(), alumnos)
    try:
        return list(alumnos_filtrados)[0]
    except:
        return {"error": "No se ha encontrado el alumno con ese nombre exacto"}

# GET por Carrera


@app.get("/alumnos/carrera/{carrera}")
async def get_alumnos_por_carrera(carrera: str):
    alumnos_filtrados = filter(
        lambda alumno: carrera.lower() in alumno.Carrera.lower(), alumnos)
    return list(alumnos_filtrados)

# GET por Edad


@app.get("/alumnos/edad/{edad}")
async def get_alumnos_por_edad(edad: int):
    alumnos_filtrados = filter(lambda alumno: alumno.Edad == edad, alumnos)
    return list(alumnos_filtrados)
