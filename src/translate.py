import json
import decimalencoder
import todoList


def translate(event, context):
        # process text
        result = todoList.get_item(event['pathParameters']['id'])
        translate = todoList.get_translate(
                result['text'],
                event['pathParameters']['lang'])
        
        if result and translate:
            result['text'] = translate
            response = {
                "statusCode": 200,
                "body": json.dumps(result,
                                    cls=decimalencoder.DecimalEncoder)
                }
        else:
            response = {
                "statusCode": 404,
                "body": ""
                }
        return response
