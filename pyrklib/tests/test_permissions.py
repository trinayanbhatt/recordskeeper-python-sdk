import unittest
import yaml
import binascii
from pyrklib import *
from pyrklib.permissions import Permissions

import sys

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


class PermissionsTest(unittest.TestCase):


    def test_grantpermissions(self):
        
        txid = Permissions.grantPermission("n33UedcQ25562cXi587hT3SpVnjsdaDGko", "create, connect")
        self.assertEqual(txid, 'Invalid permission')

    def test_revokepermissions(self):

        txid = Permissions.revokePermission("n33UedcQ25562cXi587hT3SpVnjsdaDGko", "send, admin")
        self.assertEqual(txid, 'Invalid permission')


    def test_failgrantpermissions(self):

    	txid = Permissions.grantPermission("n33UedcQ25562cXi587hT3SpVnjsdaDGko", "create, connect")
    	self.assertEqual(txid, 'e3bba87d1f0a980b65f12388d31c734ea38b08d11d00aaab1004e470ca419556')


    def test_failrevokepermissions(self):

    	txid = Permissions.revokePermission("n33UedcQ25562cXi587hT3SpVnjsdaDGko", "create, connect")
    	self.assertEqual(txid, 'e3bba87d1f0a980b65f12388d31c734ea38b08d11d00aaab1004e470ca419556')
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PermissionsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)