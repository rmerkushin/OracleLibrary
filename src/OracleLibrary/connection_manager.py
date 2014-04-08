# -*- encoding: utf-8 -*-
# Copyright (c) 2013 Roman Merkushin
# rmerkushin@ya.ru

import os
import cx_Oracle


class ConnectionManager(object):
    """
    Connection Manager handles the connection & disconnection to the database.
    """

    def __init__(self):
        """
        Initializes connection to None.
        """
        self.connection = None

    def connect_to_database(self, username, password, host, port, sid_service, encoding="American_America.AL32UTF8"):
        """
        Example usage:
        | Connect To Database | user1 | qwerty | localhost | 1521 | service=db_serv1 | Russian.AL32UTF8 |
        For set database sid: sid=db_sid_name.\n
        Encoding is optional parameter. By default is American_America.AL32UTF8.
        """
        os.environ['NLS_LANG'] = encoding
        if sid_service.split("=")[0] == "sid":
            dsn = cx_Oracle.makedsn(host, port, sid_service.split("=")[1])
        else:
            dsn = cx_Oracle.makedsn(host, port, service_name=sid_service.split("=")[1])
        self.connection = cx_Oracle.connect(username, password, dsn)

    def connect_to_database_by_tns(self, username, password, network_alias, encoding="American_America.AL32UTF8"):
        os.environ["NLS_LANG"] = encoding
        self.connection = cx_Oracle.connect(username, password, network_alias)

    def connect_to_database_by_connection_string(self, connectionString, encoding="American_America.AL32UTF8"):
        """
        Example usage:
        | Connect To Database By Connection String | user1/qwerty@localhost:1521/db_serv1 | Russian.AL32UTF8 |
        Encoding is optional parameter. By default is American_America.AL32UTF8.
        """
        os.environ['NLS_LANG'] = encoding
        self.connection = cx_Oracle.connect(connectionString)

    def disconnect_from_database(self):
        """
        Example usage:
        | Disconnect From Database | # disconnects from current connection to the database |
        """
        self.connection.close()