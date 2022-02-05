import logging

# basic configurations for logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

#  ----------------- Levels of logging

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

#  ----------------- Levels of logging

# should be imported after logging config. wont
# logout anything because propogate is set to False
import helper
