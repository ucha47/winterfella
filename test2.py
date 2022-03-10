import requests
import json
from unittest import TestCase

r = requests.get('http://api.citybik.es/v2/networks')
jsontext = r.text

parsed = json.loads(jsontext)
print(json.dumps(parsed, indent=4, sort_keys=True))


with open(jsontext, 'r') as handle:
    parsed = json.load(handle)


class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)

