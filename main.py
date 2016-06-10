# -*- coding: utf-8 -*- 
import logging
from log import __init_log_module__
from submain import *

class TestMain(object):
	LOG_FILE_NAME = "Log.log"
	"""docstring for TestMain"""
	def __init__(self, arg):
		super(TestMain, self).__init__()
		self.arg = arg
		__init_log_module__(self.LOG_FILE_NAME)

	def main(self):
		logging.info("Main test!")
		mSubmain = summain()
		mSubmain.write_log("This is sub class log!")

if __name__ == '__main__':
	mClass = TestMain("")
	mClass.main()