# -*- coding: utf-8 -*- 
import logging

def __init_log_module__(log_file_name):
	''' creat log module baisc config, log_file_name : log filename '''
	logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s - %(filename)s:[line:%(lineno)d] [%(levelname)s] %(message)s',
                # datefmt='%Y-%m-%d %H:%M:%S',  # default format is 2016-06-10 14:09:00,598
                filename=log_file_name,
                filemode='a')
	logging.debug('This is debug message')
	logging.info('This is info message')
	logging.warning('This is warning message')

