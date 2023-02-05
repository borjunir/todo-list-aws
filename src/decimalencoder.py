import decimal
import json

#Sirve para transformar un objecto de clase decimal.Decimal en int. De esta manera solucionael problema del modulo json que no sabe trabajar con objetos decimales

# This is a workaround for: http://bugs.python.org/issue16535
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)
