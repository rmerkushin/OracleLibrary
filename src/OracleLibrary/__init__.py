# -*- encoding: utf-8 -*-
# Copyright (c) 2013 Roman Merkushin
# rmerkushin@ya.ru

from connection_manager import ConnectionManager
from query import Query

__version__ = "0.1b"
__author__ = "Roman Merkushin"

class OracleLibrary(ConnectionManager, Query):

    ROBOT_LIBRARY_SCOPE = "GLOBAL"