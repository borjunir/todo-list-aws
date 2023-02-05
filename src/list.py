import json
import decimalencoder
import todoList

#Funcion que recoge todos los elementos de la lista de tareas pendientes

def list(event, context):
    # fetch all todos from the database
    result = todoList.get_items()
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result, cls=decimalencoder.DecimalEncoder)
    }
    return response
