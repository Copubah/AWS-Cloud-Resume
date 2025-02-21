import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCount')

def lambda_handler(event, context):
    response = table.get_item(Key={'id': '1'})
    count = response.get('Item', {}).get('count', 0) + 1
    table.put_item(Item={'id': '1', 'count': count})

    return {
        'statusCode': 200,
        'headers': {"Access-Control-Allow-Origin": "*"},
        'body': json.dumps({'visitor_count': count})
    }
