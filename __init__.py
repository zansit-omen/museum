import sqlite3

def set_up_database():
    conn = None
    try:
        conn = sqlite3.connect("anniversary.db")
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS photos (
                id_photo INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL,
                description TEXT NOT NULL
            );
        ''')

        # Clear old data to avoid duplicates
        cursor.execute("DELETE FROM photos")

        seed_data(cursor)

        conn.commit()

    except sqlite3.Error as e:
        print(f"Couldn't set up database due to error: {e}")
    
    finally:
        if conn:
            conn.close()
            

def seed_data(cursor):
    photos = [
        ("photos/AIGB8339.PNG", "Los quince años de Juliana, ese dia tenia las patas acalambradas de tanto bailar"),
        ("photos/BufandaAlpina.jpeg", "Esa foto me da mucha risa jajaja"),
        ("photos/CamaraCata.jpeg", "Ese dia estabamos acabando semestre y subimos a tomarnos fotos en la terraza con la camara de Catalina"),
        ("photos/AIHS2404.PNG", "Nuestro primer fin de año juntos, Ricardo nos veia tomandonos fotos, solo nos llamaba ´lamparas´ "),
        ("photos/CBLH9052.PNG", "No podia faltar la foto ridicula."),
        ("photos/IMG_1106.png", "La primera y unica vez que fuimos a piscinear."),
        ("photos/IMG_1130.PNG", "Ese dia estaba tirando unos peos hediondos yo, aun asi, como siempre, nos reiamos mucho."),
        ("photos/festivalTerror.jpeg" , "Nuestro primer festival del terror, como yo soy un viejito en el cuerpo de un man increiblemente guapo, estaba cansaito."),
        ("photos/AQWL3421.JPG", "El día que fuimos a Alpina con Natalia y Pedro, todavia me saboreo ese Alpin de chocolate, masmelos, arequipe, todo caliente."),
        ("photos/SieteMeses.jpeg", "Ese dia cumplimos siete meses, te lleve los clasicos girasoles y nos vimos en un salon porque yo tenia que hacer tareas."),
        ("photos/AZTT1119.JPG", "Nuestro primer dia de velitas juntos, ese dia casi no tome porque tenia que trabajar, tambien hablé con Don Jose acerca de nuestra relacion."),
        ("photos/Nevado.jpeg", "Ese dia probamos por primera vez el nevado de chocolate juntos, tuvimos un orgasmo oral jaja."),
        ("photos/BDDZ6595.JPEG", "El cumple de doña Graciela, el dia de ver un partido de futbol y una batalla campal. Don Jose ya queria comerse el super chicharron."),
        ("photos/IMG_0172.JPG", "Otra en Alpina, todas las fotos de ese dia me encantan, pero seleccione mis favoritas."),
        ("photos/fotoChimbo.jpeg", "No necesita explicacion."),
        ("photos/IMG_0430.JPG", "Mi cumpleaños numero veinte, por mucho, mi cumpleaños favorito, estuvieron todas las personas que amo."),
        ("photos/IMG_0989.PNG", "El mejor cumpleaños que he pasado, y ni siuquiera fue mio"),
        ("photos/IMG_0929.JPG", "Morgan estaba incomodo, sediento y adolorido, pero como a el le gusta callejear..."),
        ("photos/YKAD9143.png", "Esta foto solo me gusta mucho.")
    ]

    cursor.executemany('''
        INSERT INTO photos (url, description)
        VALUES (?, ?)
    ''', photos)


if __name__ == "__main__":
    set_up_database()