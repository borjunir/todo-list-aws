import todoList

#Funcion para eliminar tareas a partir dos parametros (evento y contexto) a traves de la funcion Lamda. De esta manera, llama a la funcion delete_item del modulo todoList
#Genera una respuesta 200 para indicar que la ejecucion ha sido existosa

def delete(event, context):
    todoList.delete_item(event['pathParameters']['id'])

    # create a response
    response = {
        "statusCode": 200
    }

    return response
