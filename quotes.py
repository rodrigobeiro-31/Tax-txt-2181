from suds.client import Client
import ssl
import datetime


if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

codigo_ISO_BCU = {'USD': 2225, 'ARS': 500, 'EUR': 1111}
codigo_BCU_ISO = {2225: 'USD', 1111: 'EUR', 501: 'ARG'}
currency_array = [501, 1111, 2225]
result = {}
updated_currency = {}


def get_rate_date():
    """ WS para obtención de la fecha de cierre (la válida) para la cotización
     return: fecha en formato aaaa-mm-dd
    """
    url = 'https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsultimocierre?WSDL'
    client = Client(url)
    try:
        result = client.service.Execute()
        fecha = result['Fecha']
    except:
        return 'Error en la fecha!!'
    return fecha


def _get_currency_list():
    """A partir de la la lista de códigos ISO de las monedas crea una lista de códigos de monedas en el formato
    esperado por el servicio awsbcucotizaciones
    """
    list = []
    for currency in currency_array:
        if codigo_BCU_ISO.has_key(currency):
            list.append(codigo_BCU_ISO.get(currency))
    return list


def get_value_from_result(result):
    for item in result['datoscotizaciones']['datoscotizaciones.dato']:
        iso = codigo_BCU_ISO.get(item['Moneda'])
        updated_currency[iso] = item['TCC']
    return True


def get_updated_currency(fecha):

    try:
        url = 'https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsbcucotizaciones?WSDL'
        client = Client(url)
        request = client.factory.create('wsbcucotizacionesin')
        array2 = client.factory.create('ArrayOfint')
        array2.item = currency_array
        request.Moneda = array2
        request.FechaDesde = fecha
        request.FechaHasta = fecha
        request.Grupo = 0
        result = client.service.Execute(request)
        value = get_value_from_result(result)

    except:
        return False
    return updated_currency


def diaAnterior(fecha):
    fechaList = fecha.split("-")
    nuevaFecha = datetime.date(int(fechaList[0]), int(fechaList[1]),
                               int(fechaList[2])) - datetime.timedelta(days=1)
    return str(nuevaFecha)


# fecha formato 'aaaa-mm-dd
def obtener_cotizaciones(fecha):
    result = get_updated_currency(fecha)
    intentos = 1
    while result == False and intentos <= 10:
        fecha = diaAnterior(fecha)
        result = get_updated_currency(fecha)
        intentos = intentos + 1

    return result


c = obtener_cotizaciones("2022-10-10")