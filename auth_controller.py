
from database import crear_conexion

def validar_credenciales(usuario, password):
    conexion = crear_conexion()

    if not conexion:
        return False

    try:
        cursor = conexion.cursor()
        query = "SELECT * FROM usuarios WHERE usuario = %s AND password = %s"
        cursor.execute(query, (usuario, password))
        resultado = cursor.fetchone()
        conexion.close()

        if resultado:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al validar credenciales: {e}")
        return False
