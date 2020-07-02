import json


def soma(event, context):
    try:
        a = int(event['queryStringParameters']['a'])
        b = int(event['queryStringParameters']['b'])
        result = a + b
    except TypeError:
        result = "Você precisa passar os parametros a e b"
    body = {
        "resultado": result
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response