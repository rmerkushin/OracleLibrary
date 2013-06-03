# -*- encoding: utf-8 -*-
# Copyright (c) 2013 Roman Merkushin
# rmerkushin@ya.ru

from connection_manager import ConnectionManager
from query import Query
from assertion import Assertion

__version__ = "0.1"
__author__ = "Roman Merkushin"

class OracleLibrary(ConnectionManager, Query, Assertion):

    ROBOT_LIBRARY_SCOPE = "GLOBAL"