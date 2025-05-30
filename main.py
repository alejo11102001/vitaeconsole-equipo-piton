# Archivo principal del sistema VitaeConsole

# Importamos los módulos necesarios
from hojasdevida import registrar_hoja_de_vida, buscar_hoja_de_vida, actualizar_hoja_de_vida
from reportes import generar_reporte, exportar_datos, reporte_por_formacion

def menu():
    while True:
        print("\n=== VitaeConsole ===")
        print("1. Registrar hoja de vida")
        print("2. Buscar hoja de vida")
        print("3. Actualizar hoja de vida")
        print("4. Generar reporte")
        print("5. Reporte por formación")
        print("6. Exportar datos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if not opcion.isdigit():
            print("\033[91m\nError: Por favor ingrese un número válido.\033[0m")
            continue

        opcion = int(opcion)
        if opcion == 1:
            registrar_hoja_de_vida()
        elif opcion == 2:
            buscar_hoja_de_vida()
        elif opcion == 3:
            actualizar_hoja_de_vida()
        elif opcion == 4:
            generar_reporte()
        elif opcion == 5:
            reporte_por_formacion()
        elif opcion == 6:
            exportar_datos()
        elif opcion == 7:
            print("\033[92mSaliendo del sistema...\033[0m")
            break
        else:
            print("\033[91mOpción inválida. Intente nuevamente.\033[0m")

if __name__ == "__main__":
    menu()
