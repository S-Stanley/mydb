#!/usr/bin/python3

import datetime as dt

def create_file_if_not_exist(table_name: str) -> bool:
    try:
        with open(f'data/{table_name}.csv', '+a') as f:
            f.read()
        return True
    except Exception as e:
        print(e)
        return False

def create_table():
    if prompt.find('CREATE TABLE ') == -1:
        return False
    if len(prompt.split(' ')) != 3:
        return False
    table_name = prompt.split('CREATE TABLE ')[1]

    create_file_if_not_exist(table_name)
    return table_name

while True:
    prompt = input('> ')
    transaction_stated = dt.datetime.now()
    table_name = create_table()

    if create_table():
        print('Executed')
        print(f'CREATED TABLE {table_name} in {(transaction_stated - dt.datetime.now()).seconds} seconds')
    else:
        print('Unknow comand')