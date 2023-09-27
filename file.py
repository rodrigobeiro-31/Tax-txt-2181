import csv

f = open('Desafio programación para FCE .csv', 'r')

csv_reader = csv.reader(f, delimiter=',')

cont = 0
fecha = []
rut = []
moneda = []
importe = []
tasa_iva = []
comprobante = []
formadepago = []
fechaAjustada = []
importeIVA = []

for fila in csv_reader:
  if cont != 0:
    ajustandoFecha2 = fila[0]
    ajustandoFecha3 = ajustandoFecha2.split("/")
    ordenFecha = [ajustandoFecha3[2], ajustandoFecha3[0], ajustandoFecha3[1]]
    ordenFecha2 = [ajustandoFecha3[2], ajustandoFecha3[0]]
    ordenFechaAjustada = "-".join(ordenFecha2)
    ajustandoFecha3 = "-".join(ordenFecha)

    fechaAjustada.append(ordenFechaAjustada)
    fecha.append(ajustandoFecha3)
    rut.append(fila[1])
    comprobante.append(fila[5])
    formadepago.append(fila[4])
    moneda.append(fila[6])
    importe.append(float(fila[7]))
    tasa_iva.append(fila[8])
    importeIVA.append("x")
  cont = cont + 1
f.close()

for i in range(1, len(moneda)):
  if moneda[i] != "UYU":
    from quotes import obtener_cotizaciones
    m = obtener_cotizaciones(fecha[i])



    if moneda[i] == "USD":
      valor1 = m["USD"]
      valor2 = importe[i]
      importe[i] = valor1 * valor2
      moneda[i] = "UYU"

    if moneda[i] == "EUR":
      valor1 = m["EUR"]
      valor2 = importe[i]
      importe[i] = valor1 * valor2
      moneda[i] = "UYU"

for i in range(0, len(tasa_iva)):
  if tasa_iva[i] == "TM":
    tasa = 0.10
    importeTotal = importe[i]
    iva = importeTotal * tasa
    importeIVA[i] = iva

  elif tasa_iva[i] == "TB":
    tasa = 0.22
    importaTotal = importe[i]
    iva = importaTotal * tasa
    importeIVA[i] = iva

  else:
    importeIVA[i] = 0

for i in range(len(formadepago)):
  if formadepago[i] == "nota_credito":
    importeIVA[i] = importeIVA[i] * -1

RUTcomprador = []
codigoimpuesto = []

for i in range(0, len(rut)):
  if len(rut[i]) > 8:
    if tasa_iva[i] == "TM":
      codigoimpuesto.append(503)
      RUTcomprador.append(rut[i])
      

    elif tasa_iva[i] == "TB":
      codigoimpuesto.append(504)
      RUTcomprador.append(rut[i])

    else:
      codigoimpuesto.append("error")
      RUTcomprador.append("error")

dic_tm = {}
dic_tb = {}
counter = 0

añonuevo = input("Ingrese un año: ")
mesnuevo = input("Ingrese un mes: ")
fechayaño = [añonuevo, mesnuevo]
fechanueva = "-".join(fechayaño)
print("Se buscaran las transacciones para la fecha: ", fechanueva)

for i in range(0, len(rut)):
  if fechanueva == fechaAjustada[i]:
    if rut.count(rut[i]) > 1:
      if "TB" in tasa_iva[i]:

        if rut[i] not in dic_tb:
          dic_tb[rut[i]] = counter + importeIVA[i]

        else:
          xa = dic_tb[rut[i]]
          dic_tb[rut[i]] = importeIVA[i] + xa

      elif "TM" in tasa_iva[i]:

        if rut[i] not in dic_tm:
          dic_tm[rut[i]] = counter + importeIVA[i]

        else:
          xa = dic_tm[rut[i]]
          dic_tm[rut[i]] = importeIVA[i] + xa

    else:

      if "TB" in tasa_iva[i]:
        dic_tb[rut[i]] = importeIVA[i]

      elif "TM" in tasa_iva[i]:
        dic_tm[rut[i]] = importeIVA[i]

RUTComprador = []
CodigoImpuesto = []
ImporteIVA1 = []

for clave in dic_tb:
  RUTComprador.append(clave)
  ImporteIVA1.append(dic_tb[clave])
  CodigoImpuesto.append(504)

for clave in dic_tm:
  RUTComprador.append(clave)
  ImporteIVA1.append(dic_tb[clave])
  CodigoImpuesto.append(503)
  

import csv

f = open('txt2181.csv', 'w')

writer = csv.writer(f, delimiter=",")
writer.writerow(["RUTComprador", "CodigoImpuesto", "ImporteIVA"])

for ww in range(0, len(RUTComprador)):
  row = [RUTComprador[ww], CodigoImpuesto[ww], ImporteIVA1[ww]]
  writer.writerow(row)

f.close()
