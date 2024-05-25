#!/usr/bin/env python3

'''Regex-ing.
'''


import logging
import re
from typing import List


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