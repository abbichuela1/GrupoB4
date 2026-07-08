Integrantes del grupo: 
Galeano, Zahira Abigail
Rodriguez, Antonella de los Ángeles
Comisión: AED 1.2
# 🎟️ Sistema de Gestión y Venta de Entradas para Recitales 
## 📝 Descripción General del Sistema
Este proyecto es una aplicación de consola desarrollada en Python que permite administrar la venta de entradas para eventos musicales. 
El sistema está diseñado para gestionar de forma eficiente la selección de sectores, el cálculo automático de importes, el control estricto de la capacidad máxima por sector 
y la aplicación de promociones (descuentos por volumen de compra). 
Además, cuenta con un módulo de persistencia de datos que guarda cada transacción, permitiendo generar estadísticas precisas sobre la recaudación total, la cantidad de entradas vendidas 
y la identificación del sector más demandado.
---
##  Instrucciones de Ejecución
### Requisitos Previos
- Tener instalado *Python 3.x* en tu sistema.
- No se requieren librerías externas (solo se utiliza el módulo estándar os).
### Pasos para ejecutar el sistema
1. Clonar este repositorio o descargar el archivo .py principal.
2. Abrir una terminal o línea de comandos.
3. Navegar hasta el directorio donde se encuentra el archivo.
4. Ejecutar el script con el siguiente comando:
   ```bash
   python recitales.py
### Uso de la IA Gemini Pro como herramienta auxiliar
La IA utilizada fue Gemini Pro, puesto que tiene un dominio bastante útil para programación, en este trabajo la utilizamos múltiples veces para corroborar nuestras correcciones a ciertos errores 
que teníamos al momento de ejecutar bloques de código.
Por ejemplo, en el control de capacidad: Decretamos que antes de concretar una venta, el sistema lee el archivo histórico, suma las entradas ya vendidas del sector solicitado y verifica que la nueva 
cantidad no supere la capacidad_max. En lugar de, como fue abordado antes del consejo de la IA; mantener una variable global en memoria que se reiniciaría si se cierra el programa. 
El sistema calcula la disponibilidad en tiempo real leyendo la fuente de verdad (el archivo de texto). Esto asegura que la validación de sobreventa sea robusta y persista entre distintas sesiones de ejecución del programa.
