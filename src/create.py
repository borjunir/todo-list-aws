import json
import logging
import todoList

#Funcion que llama a Lambda que crea un nuevo elemento en la lista de tareas
#Extrae el nombre de la tarea y su estado de check a partir de lo que se ponga en --data
#Confirma que tiene contenido ese data y sube la tarea a la BBDD ademas de contestar con un 200
#Si lo que recibe no contiene un text (nombre de tarea) genera un error

def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation failed")
        raise Exception("Couldn't create the todo item.")
    item = todoList.put_item(data['text'])
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }
    return response
