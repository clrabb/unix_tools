#!/usr/bin/python3

import unittest
import adisk_utils
from os import system
from os.path import isfile

class TestAdiskUtils(unittest.TestCase):
    def test_normalize(self):
        test_string = "_%*&$helXlo'-"
        normalized = adisk_utils.normalize_name( test_string )
        self.assertEqual( normalized, "_helxlo_" )

    def test_normalize_files(self):
        system( "touch '234_xX&^-.testme'"  )
        system( "touch 'xXxxY234_x.testme'" )
        adisk_utils.normalize_files( ".testme" )
        self.assertTrue( isfile( '234_xx_.testme' ) )
        self.assertTrue( isfile( 'xxxxy234_x.testme' ) )
        system( "rm -f *.testme" )



if __name__ == '__main__':
    unittest.main()
