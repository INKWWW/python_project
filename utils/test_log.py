#! /usr/bin/env python
# -*-coding: UTF-8-*-
#  @ Author: Wang Hanmo

import os
import logging

logging.basicConfig(filename='./record.log', level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

logging.debug("debug test")
logging.info("info test")
logging.warning("warning test")
logging.error("error test")
logging.critical('critical test')

