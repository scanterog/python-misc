import unittest
from urllib2 import urlopen, Request
import json

url = "http://127.0.0.1:5000/qengine/api/v1.0/objects"
headers = {'Content-Type': 'application/json'}


class APITest(unittest.TestCase):
    def test_store_valid_object(self):
        obj = {'identifier': 'foo', 'ranges': '[[12,34],[37,440],[460,800]]'}
        request = Request(url, json.dumps(obj), headers)
        response = urlopen(request)
        self.assertEqual(response.code, 201)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

    def test_store_empty_values(self):
        obj1 = {'identifier': '', 'ranges': '[[1,12],[15,70]]'}
        obj2 = {'identifier': '1', 'ranges': ''}
        obj3 = {'identifier': '', 'ranges': ''}

        for i in range(1, 4):
            with self.assertRaises(Exception) as context:
                response = urlopen(Request(url, json.dumps(
                    eval("obj{}".format(i))), headers))
            self.assertEqual(context.exception.code, 400)

    def test_store_malformed_request(self):
        obj1 = {'id': 1, 'ranges': ''}
        obj2 = {'identifier': '1', 'range': '[[1,2]]'}
        obj3 = {'identifier': 1, 'ranges': '[[1,2]]'}
        obj4 = {'identifier': 1.2, 'ranges': '[[1,2]]'}
        obj5 = {'identifier': '1', 'ranges': '[]'}
        obj6 = {'identifier': '1', 'ranges': '[[]]'}
        obj7 = {'identifier': '1', 'ranges': '[[1]]'}
        obj8 = {'identifier': '1', 'ranges': '[[1],[2]]'}
        obj9 = {'identifier': '1', 'ranges': '[(1)]'}
        obj10 = {'identifier': '1', 'ranges': '[(1),(2)]'}
        obj11 = {'identifier': '1', 'ranges': '[1,2]'}
        obj12 = {'identifier': '1', 'ranges': '1'}
        obj13 = {'identifier': '1', 'ranges': '1,2'}
        obj14 = {'identifier': '1', 'ranges': '(1,2)'}

        for i in range(1, 15):
            with self.assertRaises(Exception) as context:
                response = urlopen(Request(url, json.dumps(
                    eval("obj{}".format(i))), headers))
            self.assertEqual(context.exception.code, 400)

    def test_store_overwrite_object(self):
        obj1 = {'identifier': 'foo', 'ranges': '[[12,34],[37,440],[460,800]]'}
        obj2 = {'identifier': 'foo', 'ranges': '[[1,2]]'}
        for i in range(1, 3):
            response = urlopen(Request(url, json.dumps(
                eval("obj{}".format(i))), headers))
        data = response.read()
        obj_list = json.loads(data)
        for o in obj_list:
            if o['identifier'] == 'foo':
                self.assertEqual(o['ranges'], [[1, 2]])
                break

    def test_retrieve_overlapped_object(self):
        start_range = 450
        end_range = 464
        qurl = url + "/" + str(start_range) + "/" + str(end_range)
        # load data
        obj = {'identifier': 'foo', 'ranges': '[[12,34],[37,440],[460,800]]'}
        urlopen(Request(url, json.dumps(obj), headers))
        # retrieve
        request = Request(qurl)
        response = urlopen(request)
        data = response.read()
        obj_list = json.loads(data)
        self.assertEqual(obj_list[0]['intersection'], 4)

if __name__ == '__main__':
    unittest.main()
