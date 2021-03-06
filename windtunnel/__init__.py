# -*- coding: utf-8 -*-
"""Python package for use with BSA software output.
"""

import logging
import os

from .utils import *
from .stats import *
from . import plots
from .timeseries import *

# set standards for Logging module
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='log_file.txt'.format(os.getlogin()),
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logger = logging.getLogger('')
logger.addHandler(console)


__all__ = [s for s in dir() if not s.startswith('_')]