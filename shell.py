#!/usr/bin/env python3
import os
import sys

if sys.platform != 'ios': # Not Pythonista
	import readline

from pprint import pprint

from flask import *
from app import *

os.environ['PYTHONINSPECT'] = 'True'
