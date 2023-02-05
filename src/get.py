import json
import decimalencoder
import todoList

#Funcion Lamda para recoger la informacion de una tarea a partir del id de esta

def get(event, context):
    # create a response
    item = todoList.get_item(event['pathParameters']['id'])
    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response
