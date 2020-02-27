import sqlite3
import os


def create_connection(db_name):
    '''
    Функция создает соединение с БД db_name
    и возвращает его
    '''
    connection = sqlite3.connect(db_name)
    return connection
    
def create_tables(schema, connection):
    try:
        print('Creating schema...')
        with open(schema, 'r') as f:
            blueprint = f.read()
            connection.executescript(blueprint)
        print('Done!')
    except sqlite3.OperationalError as e:
        print('Error occured: ', e)
    
if __name__ == '__main__':
    db_exists = os.path.exists('dhcp_snooping.db')
    con = create_connection('dhcp_snooping.db')
    
    if db_exists:
        create_tables('dhcp_snooping_schema.sql', con)
    else:
        print('Database exists.')
        
    

    
        
        
        
