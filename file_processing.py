#!/usr/bin/python
#-*- coding: utf-8 -*-

u'''
Copyright (c) Telefonica I+D. All rights reserved.
Description: Example of processing files with encoding
'''

def insert_line(cursor, line):
    sql = 'INSERT INTO CUSTOMERS VALUES (?,?,?,?,?,?,?,?,?)'
    cursor.execute(sql, line)


def process_file_db(connection, file_path):
    try:
        cursor = connection.cursor()
        with open(file_path, 'r') as opened_file:
            headers = opened_file.readline()
            for line in opened_file.readlines():
                insert_line(cursor, line.rstrip().split('|'))
    finally:
        cursor.close()
    
def process_csv_db(connection, file_path):
    try:
        connection.text_factory = str
        cursor = connection.cursor()
        with open(file_path, 'r') as opened_file:
            import csv
            reader = csv.reader(opened_file, delimiter=('|'))
            headers = reader.next()
            for line in reader:
                insert_line(cursor, line)
    finally:
        cursor.close()
    
def process_codecs_db(connection, file_path):
    try:
        cursor = connection.cursor()
        import codecs
        with codecs.open(file_path) as opened_file:
            for i, line in enumerate(opened_file.readlines()):
                if i != 0:
                    insert_line(cursor, line.rstrip().split('|'))
    finally:
        cursor.close()

def process_codecs_file(file_path_in, file_path_out):
    import codecs
    with codecs.open(file_path_in) as read_file:
        with codecs.open(file_path_out, 'w+') as write_file:
            for line in read_file:
                write_file.write(line)


