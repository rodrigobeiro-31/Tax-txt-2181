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
resulta1 = []
importeIVA = []

for fila in csv_reader:
  if cont != 0:
    fecha2 = fila[0]
    fecha3 = fecha2.split("/")
    result = [fecha3[2], fecha3[0], fecha3[1]]
    result1 = [fecha3[2], fecha3[0]]
    result2 = "-".join(result1)
    fecha3 = "-".join(result)

    resulta1.append(result2)
    fecha.append(fecha3)
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
      valorr1 = m["USD"]
      valorr2 = importe[i]
      importe[i] = valorr1 * valorr2
      moneda[i] = "UYU"

    if moneda[i] == "EUR":
      valor1 = m["EUR"]
      valor2 = importe[i]
      importe[i] = valor1 * valor2
      moneda[i] = "UYU"

for a in range(0, len(tasa_iva)):
  if tasa_iva[a] == "TM":
    tasa1 = 0.10
    tasa2 = importe[a]
    tasa3 = tasa2 * tasa1
    importeIVA[a] = tasa3

  elif tasa_iva[a] == "TB":
    tasa4 = 0.22
    tasa5 = importe[a]
    tasa6 = tasa5 * tasa4
    importeIVA[a] = tasa6

  else:
    importeIVA[a] = 0

for am in range(len(formadepago)):
  if formadepago[am] == "nota_credito":
    importeIVA[am] = importeIVA[am] * -1

RUTcomprador = []
codigoimpuesto = []

for ii in range(0, len(rut)):
  if len(rut[ii]) > 8:
    if tasa_iva[ii] == "TM":
      codigoimpuesto.append(503)
      RUTcomprador.append(rut[ii])
      

    elif tasa_iva[ii] == "TB":
      codigoimpuesto.append(504)
      RUTcomprador.append(rut[ii])

    else:
      codigoimpuesto.append("error")
      RUTcomprador.append("error")

dic_tm = {}
dic_tb = {}
contator = 0

añonuevo = input("Ingrese un año: ")
mesnuevo = input("Ingrese un mes: ")
fechayaño = [añonuevo, mesnuevo]
fechanueva = "-".join(fechayaño)
print("Se buscaran las transacciones para la fecha: ", fechanueva)

for aa in range(0, len(rut)):
  if fechanueva == resulta1[aa]:
    if rut.count(rut[aa]) > 1:
      if "TB" in tasa_iva[aa]:

        if rut[aa] not in dic_tb:
          dic_tb[rut[aa]] = contator + importeIVA[aa]

        else:
          xa = dic_tb[rut[aa]]
          dic_tb[rut[aa]] = importeIVA[aa] + xa

      elif "TM" in tasa_iva[aa]:

        if rut[aa] not in dic_tm:
          dic_tm[rut[aa]] = contator + importeIVA[aa]

        else:
          xa = dic_tm[rut[aa]]
          dic_tm[rut[aa]] = importeIVA[aa] + xa

    else:

      if "TB" in tasa_iva[aa]:
        dic_tb[rut[aa]] = importeIVA[aa]

      elif "TM" in tasa_iva[aa]:
        dic_tm[rut[aa]] = importeIVA[aa]

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
