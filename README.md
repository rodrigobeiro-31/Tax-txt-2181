# Desafío Programación para FCE

Este script en Python procesa un archivo CSV que contiene datos de transacciones financieras y genera un nuevo archivo CSV que resume la información por comprador y tipo de impuesto. El proceso implica calcular el importe del IVA, realizar conversiones de moneda y consolidar la información.

## Funcionalidades

1. **Procesamiento de Datos**: Lee un archivo CSV que contiene transacciones financieras y extrae la información relevante, incluyendo fechas, RUT del comprador, moneda, importe, tasa de IVA, y forma de pago.

2. **Conversión de Moneda**: Convierte los importes a la moneda local (UYU) usando tasas de cambio obtenidas externamente.

3. **Cálculo del IVA**: Calcula el importe del IVA en función de la tasa de IVA y el importe de la transacción.

4. **Agrupación por Comprador y Tipo de Impuesto**: Agrupa las transacciones por RUT del comprador y tipo de impuesto (TM o TB) y suma los importes de IVA correspondientes.

5. **Generación de Archivo de Salida**: Crea un nuevo archivo CSV que contiene la información resumida por RUT del comprador, tipo de impuesto y el importe total del IVA.

## Uso

1. **Ejecución**: Para buscar transacciones correspondientes a un mes y año específicos, ejecuta el script proporcionando el año y el mes como argumentos. Asegúrate de seleccionar los meses disponibles en el archivo CSV "Desafio programación para FCE" para probar el funcionamiento adecuado (2022-10/2022-9/2022-8).

2. **Entrada**: El script requiere un archivo CSV con un formato específico. Utiliza este archivo como entrada, ya que la información contenida en él será la base para realizar los cálculos necesarios

3. **Salida**: Después de procesar la información correspondiente al mes y año especificados, el script generará un archivo CSV de salida. Este archivo contendrá la información consolidada según los parámetros proporcionados.

## Dependencias

Asegúrate de tener instaladas las siguientes dependencias antes de ejecutar el script:

- suds: Se utiliza para consumir servicios web SOAP en Python.

## Notas Adicionales

- Asegúrate de tener el archivo CSV adecuado antes de ejecutar el script.

---

Este proyecto es parte del Desafío de Programación para FCE y demuestra la habilidad para manipular datos financieros, realizar cálculos complejos y generar informes resumidos para su posterior procesamiento en plataformas como la Dirección General Impositiva (DGI).
