import logging

try:
    a = 5/0
except ZeroDivisionError as e:
    logging.error(e, exc_info=True)
