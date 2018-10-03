import logging

#logging.basicConfig(filename='logging.log',level=logging.DEBUG, format='')





#logging.basicConfig(filename='x.log', level= logging.DEBUG, format='')%(asctime)s:%(levelname)s:%(message)s


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('x.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)
logger.error(10/0)



