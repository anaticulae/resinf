#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import os

from resinf.configure import mainpackage
from resinf.configure import setup
from resinf.configure import worker_count
from resinf.path import Todo
from resinf.path import bypages
from resinf.path import generated
from resinf.path import link
from resinf.path import pdf
from resinf.path import prepares
from resinf.path import simple
from resinf.path import todo
from resinf.path import todo_new

from resinf.hard import *  # isort:skip

__version__ = '0.4.0'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
