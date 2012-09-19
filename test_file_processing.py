#!/usr/bin/python
#-*- coding: utf-8 -*-

import file_processing as exercise
import unittest

import sqlite3

class TestExercise(unittest.TestCase):
    """Test for exercise"""

    def setUp(self):
        self.connection = sqlite3.connect('test.db')
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM customers')
        cursor.close()
    
    def tearDown(self):
        self.connection.close()


    def test_process_file_db_utf8(self):
        """ Try to process a file with open builtin function and inserting into
        db"""
        file_path = 'test-utf8.dat'
        self.connection.text_factory = str
        exercise.process_file_db(self.connection, file_path)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM CUSTOMERS WHERE NAME LIKE "Magda%"')
        self.assertEqual(cursor.fetchone()[0].decode('utf-8'), u'Magdalena Díaz')
        cursor.close()

    def test_process_file_db_latin1(self):
        """ Try to process a file with open builtin function and inserting into
        db. Test with latin1 input file."""
        file_path = 'test-latin1.dat'
        self.connection.text_factory = str
        exercise.process_file_db(self.connection, file_path)
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM CUSTOMERS WHERE NAME LIKE "Magda%"')
        self.assertEqual(cursor.fetchone()[0].decode('utf-8'), u'Magdalena Díaz')
        cursor.close()
            
    def test_process_file_utf8(self):
        with open('test-utf8.dat', 'r') as filep:
            for line in filep.readlines():
                print line
                print 'Decoded line: {0}'.format(line.decode('utf-8'))

    def test_process_csv_db_utf8(self):
        """ Try to process a file with csv module and inserting into
        db"""
        file_path = 'test-utf8.dat'
        exercise.process_csv_db(self.connection, file_path)
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM CUSTOMERS WHERE NAME LIKE "Magda%"')
        self.assertEqual(cursor.fetchone()[0], u'Magdalena Díaz')
        cursor.close()

    def test_process_csv_db_latin1(self):
        """ Try to process a file with csv module and inserting into
        db. Test with latin1 input file."""
        file_path = 'test-latin1.dat'
        exercise.process_csv_db(self.connection, file_path)
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM CUSTOMERS WHERE NAME LIKE "Magda%"')
        self.assertEqual(cursor.fetchone()[0], u'Magdalena Díaz')
        cursor.close()

    def test_process_codecs_db_utf8(self):
        """ Try to process a file with codecs module and inserting into
        db."""
        file_path = 'test-utf8.dat'
        exercise.process_codecs_db(self.connection, file_path)
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM CUSTOMERS WHERE NAME LIKE "Magda%"')
        self.assertEqual(cursor.fetchone()[0], u'Magdalena Díaz')
        cursor.close()

    def test_process_codecs_db_latin1(self):
        """ Try to process a file with codecs module and inserting into
        db. Test with latin1 file."""
        file_path = 'test-latin1.dat'
        exercise.process_codecs_db(self.connection, file_path)
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM CUSTOMERS WHERE NAME LIKE "Magda%"')
        self.assertEqual(cursor.fetchone()[0], u'Magdalena Díaz')
        cursor.close()

    def test_process_codecs_file_utf8(self):
        """ Process a file and write it to another file. output in utf-8
        """
        in_file = 'test-utf8.dat'
        out_file = 'test-out-utf8.dat'
        exercise.process_codecs_file(in_file, out_file)
        with open(out_file) as assert_file:
            for line in assert_file:
                name = line.rstrip().split('|')[0]
                if name.startswith('Mag'):
                    self.assertEqual(name, u'Magdalena Díaz')

    def test_process_codecs_file_latin1(self):
        """ Process a file in latin1 and write it to another file. output in utf-8
        """
        in_file = 'test-latin1.dat'
        out_file = 'test-out-utf8.dat'
        exercise.process_codecs_file(in_file, out_file)
        with open(out_file) as assert_file:
            for line in assert_file:
                name = line.rstrip().split('|')[0]
                if name.startswith('Mag'):
                    self.assertEqual(name, u'Magdalena Díaz')



if __name__ == '__main__':
    unittest.main()
