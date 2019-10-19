import base64
import json

def serialize_payload(payload):
    json_str = json.dumps(payload) + "\n"
    json_bytes = bytes(json_str, 'utf8')
    b64_bytes = base64.b64encode(json_bytes)
    b64_str = b64_bytes.decode('utf8')
    return b64_str

def lambda_handler(event, context):
    output = []

    for record in event['records']:
        json_payload = base64.b64decode(record['data'])
        payload = json.loads(json_payload)
        data_dict = json.loads(payload['data'])
        payload['data'] = data_dict
        record_data = serialize_payload(payload)

        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': record_data
        }
        output.append(output_record)

        return { 'records': output }
