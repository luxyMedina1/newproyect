
from auth_controller import validar_credenciales

print(" PRUEBA COMPLETA DEL SISTEMA")
print("=" * 40)


def ver_usuarios():
    """Función de compatibilidad usada por la interfaz gráfica.
    Devuelve una lista de tuplas (id, usuario). Reemplázala por acceso real a la BD cuando lo tengas.
    """
    return [
        (1, "lucia"),
        (2, "Admin"),
    ]

# Probar con credenciales correctas
print("\n1. Probando con credenciales CORRECTAS:")
resultado1 = validar_credenciales("Lucia", "1234")
print(f"Resultado: {resultado1}")

# Probar con credenciales incorrectas
print("\n2. Probando con credenciales INCORRECTAS:")
resultado2 = validar_credenciales("Yadira", "wrongpassword")
print(f"Resultado: {resultado2}")

# Probar con usuario que no existe
print("\n3. Probando con usuario INEXISTENTE:")
resultado3 = validar_credenciales("UsuarioInexistente", "1234")
print(f"Resultado: {resultado3}")

print("\n" + "=" * 40)
if resultado1:
    print(" ¡EL SISTEMA FUNCIONA CORRECTAMENTE!")
else:
    print(" Hay problemas en el sistema")