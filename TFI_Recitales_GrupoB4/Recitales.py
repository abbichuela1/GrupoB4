import os

# --- CONFIGURACIÓN Y ESTRUCTURA DE DATOS ---
ARCHIVO_VENTAS = "ventas.txt"
# Módulo 3: Diccionario para gestionar capacidad y precios de forma eficiente
SECTORES = {
    'A': {'precio': 5000, 'capacidad_max': 10},
    'B': {'precio': 3000, 'capacidad_max': 20},
    'C': {'precio': 1500, 'capacidad_max': 30}
}

# --- FUNCIONES (MODULARIZACIÓN) ---

def calcular_descuento(total, cantidad):
    """Aplica descuento del 10% si la compra es mayor a 5 entradas."""
    if cantidad > 5:
        print("¡Promoción aplicada: 10% de descuento por cantidad!")
        return total * 0.90
    return total

def obtener_ventas_actuales():
    """Calcula cuántas entradas se han vendido por sector leyendo el archivo."""
    ventas = {'A': 0, 'B': 0, 'C': 0}
    if os.path.exists(ARCHIVO_VENTAS):
        try:
            with open(ARCHIVO_VENTAS, 'r') as f:
                for linea in f:
                    datos = linea.strip().split(',')
                    if len(datos) >= 2:
                        ventas[datos[0]] += int(datos[1])
        except Exception as e:
            print(f"Error al leer datos del archivo: {e}")
    return ventas

def registrar_venta():
    """Gestiona el flujo de venta, validaciones y persistencia."""
    print("\n--- Registro de Venta ---")
    
    # Muestra de precios (UX)
    print("Precios vigentes por sector:")
    for sector, datos in SECTORES.items():
        print(f"Sector {sector}: ${datos['precio']} (Capacidad máx: {datos['capacidad_max']})")
    
    sector = input("\nIngrese sector deseado (A($5000)/B($3000)/C($1500)): ").upper()
    
    if sector not in SECTORES:
        print("Error: Sector no válido.")
        return

    try:
        cantidad = int(input("Ingrese cantidad de entradas: "))
        
        # Control de capacidad
        ventas = obtener_ventas_actuales()
        if ventas[sector] + cantidad > SECTORES[sector]['capacidad_max']:
            disponibles = SECTORES[sector]['capacidad_max'] - ventas[sector]
            print(f"Error: No hay capacidad suficiente. Disponibles: {disponibles}")
            return

        subtotal = SECTORES[sector]['precio'] * cantidad
        total_final = calcular_descuento(subtotal, cantidad)
        
        # Módulo 4: Guardado persistente
        with open(ARCHIVO_VENTAS, 'a') as f:
            f.write(f"{sector},{cantidad},{total_final:.2f}\n")
        
        print(f"-----------------------------------")
        print(f"Resumen: {cantidad} entradas de sector {sector}")
        print(f"Total a pagar: ${total_final:.2f}")
        print(f"-----------------------------------")

    except ValueError:
        print("Error: Ingrese un valor numérico válido.")

def ver_estadisticas():
    """Calcula y muestra estadísticas usando contadores y acumuladores."""
    ventas = obtener_ventas_actuales()
    recaudacion = 0
    
    if os.path.exists(ARCHIVO_VENTAS):
        with open(ARCHIVO_VENTAS, 'r') as f:
            for linea in f:
                datos = linea.strip().split(',')
                if len(datos) == 3:
                    recaudacion += float(datos[2])

    print("\n--- Estadísticas de Ventas ---")
    if sum(ventas.values()) > 0:
        # Identificación del sector más demandado
        sector_mas_vendido = max(ventas, key=ventas.get)
        for s, c in ventas.items():
            print(f"Sector {s}: {c} entradas vendidas")
        print(f"Recaudación total: ${recaudacion:.2f}")
        print(f"Sector más demandado: {sector_mas_vendido}")
    else:
        print("Aún no hay ventas registradas.")

def main():
    """Menú principal (Estructura iterativa)."""
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE RECITALES ---")
        print("1. Registrar venta | 2. Ver estadísticas | 3. Salir")
        opcion = input("Seleccione: ")
        if opcion == '1': registrar_venta()
        elif opcion == '2': ver_estadisticas()
        elif opcion == '3': 
            print("Cerrando sistema...")
            break
        else: print("Opción inválida.")

if __name__ == "__main__":
    main()