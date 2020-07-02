import json


def soma(event, context):
    try:
        a = int(event['queryStringParameters']['a'])
        b = int(event['queryStringParameters']['b'])
        result = a + b
    except TypeError:
        result = 0
    body = {
        "resultado": result
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response