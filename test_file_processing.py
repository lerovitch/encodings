#!/usr/bin/python
#-*- coding: utf-8 -*-

import unittest

CHECK_UTF8 = 'Esto es una prueba s\xc3\xbaper raruna \xc3\xa0\xc3\xa4\xc3\xa2y\xc2\xa5\xe2\x82\xac\xc3\xa5'
CHECK_LATIN1 = 'Esto es una prueba s\xfaper raruna \xe0\xe4\xe2y\xa5\xe5'

CHECK_UNICODE = u'Esto es una prueba s\u00FAper raruna \u00E0\u00E4\u00E2y\u00A5\u00E5'


class TestExercise(unittest.TestCase):
    """Test for exercise"""

    def test_process_file_utf8(self):
        file_path = 'test-utf8.dat'
        with open(file_path, 'r') as opened_file:
            line = opened_file.readline().strip()
            self.assertEqual(line, CHECK_UTF8)

    def test_process_file_latin1(self):
        file_path = 'test-latin1.dat'
        with open(file_path, 'r') as opened_file:
            line = opened_file.readline().strip()
            self.assertEqual(line, CHECK_LATIN1)

    def test_process_file_utf8_to_latin1(self):
        file_path = 'test-utf8.dat'
        with open(file_path, 'r') as opened_file:
            line = opened_file.readline().strip()
            self.assertEqual(line, CHECK_LATIN1)

    def test_process_file_latin1_to_unicode(self):
        file_path = 'test-latin1.dat'
        with open(file_path, 'r') as opened_file:
            line = opened_file.readline().strip()
            self.assertEqual(line, CHECK_UNICODE)

    def test_process_file_utf8_decoded(self):
        with open('test-utf8.dat', 'r') as filep:
            for line in filep.readlines():
                print line
                print 'Decoded line: {0}'.format(line.decode('utf-8'))



if __name__ == '__main__':
    unittest.main()
