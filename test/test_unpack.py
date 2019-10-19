import unittest
import base64
import json

from lambda_function.unpack import lambda_handler

EVENT = {
    'records': [
        {
            'recordId': 123456789,
            'result': 'Ok',
            'data': 'eyJkYXRhIjogIntcImZvb1wiOlwiYmFyXCJ9In0=' # contains { "data": "{\"foo\" : \"bar\"}" }
        }
    ]
}

class TestUnpack(unittest.TestCase):
    
    def test_lambda_handler(self):
        output = lambda_handler(EVENT, {})

        self.assertEqual(len(output['records']), 1)
        self.assertEqual(output['records'][0]['recordId'], EVENT['records'][0]['recordId'])
        self.assertEqual(output['records'][0]['result'], EVENT['records'][0]['result'])

        data_str = base64.b64decode(output['records'][0]['data']).decode('utf-8')
        data_json = json.loads(data_str)
        self.assertEqual(data_json['data'], { 'foo': 'bar' })

if __name__ == "__main__":
    unittest.main()
