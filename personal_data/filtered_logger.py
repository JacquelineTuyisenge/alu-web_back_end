#!/usr/bin/env python3

'''Regex-ing.
'''


import logging
import re
import os
import mysql.connector  # type: ignore
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''should use a regex to replace occurrences of certain field values..
    '''
    pattern = '|'.join([f'{field}=[^{separator}]*' for field in fields])
    return re.sub(
        pattern,
        lambda m: m.group(0).split('=')[0] + '=' + redaction,
        message
    )


def get_logger() -> logging.Logger:
    """ Implementing a logger.
    """

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """


    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        ''' Constructor for RedactingFormatter class'''
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        ''' Formatting function'''
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)

def get_db() -> mysql.connector.connection.MySQLConnection:
    '''Establish a connection to the database and return a connection object.'''


    user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    if database is None:
        raise ValueError("Database name must be in environment variable")

    return mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )

def main() -> None:
    ''' main function'''

    logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO)
    logger = logging.getLogger('user_data')

    fields = ['name', 'email', 'phone', 'ssn', 'password']

    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT name, email, phone, ssn, password, ip, last_login, user_agent FROM users")
    rows = cursor.fetchall()

    for row in rows:
        message = f"name={row[0]}; email={row[1]}; phone={row[2]}; ssn={row[3]}; password={row[4]}; ip={row[5]}; last_login={row[6]}; user_agent={row[7]}"
        filtered_message = filter_datum(fields, '***', message, '; ')
        logger.info(filtered_message)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
