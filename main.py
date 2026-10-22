"""
PFU-111 - Semana 12
Sistema de registro de solicitudes de soporte técnico
Integrantes:
- Elvis Quispe Mamani
- Hugo Marcelo Nina Garcia
- Brayan Oruña Guarachi
- Adriana Micaela Torrejon Peña

Ejecución: python main.py
"""

from dataclasses import dataclass
import re


TIPOS_VALIDOS = {"equipo", "software", "conectividad"}
PRIORIDADES_VALIDAS = {"baja", "media", "alta"}
# Regla implementada para el código: 6 a 12 caracteres alfanuméricos.
# Verificar con el docente si la guía establece un formato institucional distinto.
PATRON_CODIGO = re.compile(r"^[A-Za-z0-9]{6,12}$")


@dataclass
class Solicitud:
    nombre: str
    codigo: str
    tipo: str
    descripcion: str
    prioridad: str


def validar_solicitud(nombre, codigo, tipo, descripcion, prioridad):
    """Devuelve una lista de errores; lista vacía significa que todo es válido."""
    errores = []
    if not nombre.strip():
        errores.append("El nombre no puede estar vacío.")
    if not PATRON_CODIGO.fullmatch(codigo.strip()):
        errores.append("El código debe tener entre 6 y 12 caracteres alfanuméricos.")
    if tipo.strip().lower() not in TIPOS_VALIDOS:
        errores.append("El tipo debe ser: equipo, software o conectividad.")
    if not descripcion.strip():
        errores.append("La descripción no puede estar vacía.")
    if prioridad.strip().lower() not in PRIORIDADES_VALIDAS:
        errores.append("La prioridad debe ser: baja, media o alta.")
    return errores


def leer_no_vacio(mensaje):
    """Lee texto y deja que el usuario corrija una entrada vacía."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: este campo no puede quedar vacío. Intente nuevamente.")


def registrar_solicitud():
    print("\n--- Registrar solicitud ---")
    nombre = input("Nombre completo: ").strip()
    codigo = input("Código de estudiante (6-12 letras/números): ").strip()
    tipo = input("Tipo (equipo/software/conectividad): ").strip().lower()
    descripcion = input("Descripción del problema: ").strip()
    prioridad = input("Prioridad (baja/media/alta): ").strip().lower()

    errores = validar_solicitud(nombre, codigo, tipo, descripcion, prioridad)
    if errores:
        print("\nNo se registró la solicitud:")
        for error in errores:
            print(f"- {error}")
        return None

    solicitud = Solicitud(nombre, codigo, tipo, descripcion, prioridad)
    print("\nSolicitud registrada correctamente.")
    return solicitud


def mostrar_solicitud(solicitud):
    if solicitud is None:
        print("\nNo hay ninguna solicitud registrada.")
        return
    print("\n--- Solicitud registrada ---")
    print(f"Solicitante : {solicitud.nombre}")
    print(f"Código      : {solicitud.codigo}")
    print(f"Tipo        : {solicitud.tipo}")
    print(f"Descripción : {solicitud.descripcion}")
    print(f"Prioridad   : {solicitud.prioridad}")


def limpiar_datos():
    """En una aplicación de consola, limpiar significa reiniciar el formulario."""
    print("\nFormulario reiniciado. Puede ingresar una nueva solicitud.")


def main():
    solicitud_actual = None
    while True:
        print("\n====== SISTEMA DE SOPORTE TÉCNICO ======")
        print("1. Registrar solicitud")
        print("2. Limpiar / reiniciar formulario")
        print("3. Consultar solicitud")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ").strip()

        try:
            if opcion == "1":
                nueva = registrar_solicitud()
                if nueva is not None:
                    solicitud_actual = nueva
            elif opcion == "2":
                solicitud_actual = None
                limpiar_datos()
            elif opcion == "3":
                mostrar_solicitud(solicitud_actual)
            elif opcion == "4":
                print("Programa finalizado. ¡Hasta luego!")
                break
            else:
                raise ValueError("Seleccione una opción del 1 al 4.")
        except (ValueError, EOFError) as error:
            print(f"Entrada no válida: {error}. Intente nuevamente.")
        except KeyboardInterrupt:
            print("\nInterrupción detectada. Puede volver al menú o salir con la opción 4.")


if __name__ == "__main__":
    main()
