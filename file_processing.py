#!/usr/bin/python
#-*- coding: utf-8 -*-

u'''
Copyright (c) Telefonica I+D. All rights reserved.
Description: Example of processing files with encoding
'''

import sqlite3;

def insert_line(cursor, line):
    sql = 'INSERT INTO CUSTOMERS VALUES (?,?,?,?,?,?,?,?,?)'
    cursor.execute(sql, line)


def process_file_db(file_path, encoding):
    with sqlite3.connect('test.db') as connection:
        cursor = connection.cursor()
        with open(file_path, 'r') as opened_file:
            headers = opened_file.readline()
            for line in opened_file.readlines():
                line = line.decode(encoding)
                insert_line(cursor, line.rstrip().split('|'))
        cursor.close()
    
def process_csv_db(file_path, encoding):
    with sqlite3.connect('test.db') as connection:
        connection.text_factory = str
        cursor = connection.cursor()
        with open(file_path, 'r') as opened_file:
            import csv
            reader = csv.reader(opened_file, delimiter=('|'))
            headers = reader.next()
            for line in reader:
                line = [value.decode(encoding) for value in line]
                insert_line(cursor, line)
        cursor.close()
    
def process_codecs_db(file_path, encoding):
    with sqlite3.connect('test.db') as connection:
        cursor = connection.cursor()
        import codecs
        with codecs.open(file_path, encoding=encoding) as opened_file:
            for i, line in enumerate(opened_file.readlines()):
                if i != 0:
                    insert_line(cursor, line.rstrip().split('|'))

def process_codecs_file(file_path_in, file_path_out, encoding_in, encoding_out):
    import codecs
    with codecs.open(file_path_in, encoding=encoding_in) as read_file:
        with codecs.open(file_path_out, 'w+', encoding=encoding_out) as write_file:
            for line in read_file:
                write_file.write(line)


