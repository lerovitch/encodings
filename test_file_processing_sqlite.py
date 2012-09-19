#!/usr/bin/python
#-*- coding: utf-8 -*-

import file_processing as exercise
import unittest

import sqlite3

FILE_UTF8 = 'test-utf8-db.dat'
FILE_LATIN1 = 'test-latin1-db.dat'

class TestExercise(unittest.TestCase):

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
        self.connection.text_factory = str
        cursor = self.connection.cursor()
        exercise.process_file_db(cursor, FILE_UTF8)
        cursor.execute('SELECT * FROM CUSTOMERS WHERE NAME LIKE "Magda%"')
        self.assertEqual(cursor.fetchone()[0].decode('utf-8'), u'Magdalena Díaz')
        cursor.close()

    def test_process_file_db_latin1(self):
        """ Try to process a file with open builtin function and inserting into
        db. Test with latin1 input file."""
        self.connection.text_factory = str
        exercise.process_file_db(self.connection, FILE_LATIN1)
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM CUSTOMERS WHERE NAME LIKE "Magda%"')
        self.assertEqual(cursor.fetchone()[0].decode('utf-8'), u'Magdalena Díaz')
        cursor.close()
            

    def test_process_csv_db_utf8(self):
        """ Try to process a file with csv module and inserting into
        db"""
        exercise.process_csv_db(self.connection, FILE_UTF8)
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM CUSTOMERS WHERE NAME LIKE "Magda%"')
        self.assertEqual(cursor.fetchone()[0], u'Magdalena Díaz')
        cursor.close()

    def test_process_csv_db_latin1(self):
        """ Try to process a file with csv module and inserting into
        db. Test with latin1 input file."""
        exercise.process_csv_db(self.connection, FILE_LATIN1)
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM CUSTOMERS WHERE NAME LIKE "Magda%"')
        self.assertEqual(cursor.fetchone()[0], u'Magdalena Díaz')
        cursor.close()

    def test_process_codecs_db_utf8(self):
        """ Try to process a file with codecs module and inserting into
        db."""
        exercise.process_codecs_db(self.connection, FILE_UTF8)
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM CUSTOMERS WHERE NAME LIKE "Magda%"')
        self.assertEqual(cursor.fetchone()[0], u'Magdalena Díaz')
        cursor.close()

    def test_process_codecs_db_latin1(self):
        """ Try to process a file with codecs module and inserting into
        db. Test with latin1 file."""
        exercise.process_codecs_db(self.connection, FILE_LATIN1)
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM CUSTOMERS WHERE NAME LIKE "Magda%"')
        self.assertEqual(cursor.fetchone()[0], u'Magdalena Díaz')
        cursor.close()

    def test_process_file_latin1(self):
        """ Process a file and write it to another file with caps.
        """
        print ' a'
        exercise.process_file(FILE_LATIN1, FILE_LATIN1 + '.out')
        with open(FILE_LATIN1+ '.out') as assert_file:
            for line in assert_file:
                self.assertEqual(line.endswith('€'))


if __name__ == '__main__':
    unittest.main()
