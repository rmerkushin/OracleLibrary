# -*- encoding: utf-8 -*-
# Copyright (c) 2013 Roman Merkushin
# rmerkushin@ya.ru

from robot.api import logger

class Query(object):
    """
    Query handles all the querying done by the Oracle Library.
    """

    def query(self, selectStatement):
        """
        Executes the selectStatement as SQL command and return query result.\n
        Example usage:
        | @{queryResult} | Query | SELECT * FROM NLS_DATABASE_PARAMETERS |
        | Log Many | @{queryResult} |
        """
        cursor = None
        try:
            cursor = self.connection.cursor()
            self.__execute_sql(cursor, selectStatement)
            allRows = cursor.fetchall()
            i = 0
            for x in allRows:
                allRows[i] = map(lambda s: str(s).decode("utf-8"), x)
                i += 1
            return allRows
        finally:
            if cursor:
                self.connection.rollback()

    def query_result_as_one_row(self, selectStatement):
        cursor = None
        try:
            cursor = self.connection.cursor()
            self.__execute_sql(cursor, selectStatement)
            allRows = cursor.fetchall()
            result = []
            for row in allRows:
                for x in row:
                    result.append(str(x).decode("utf-8"))
            return result
        finally:
            if cursor:
                self.connection.rollback()

    def row_count(self, selectStatement):
        """
        Uses the input `selectStatement` to query the database and returns the number of rows from the query.\n
        Example usage:
        | ${rowCount} | Row Count | SELECT * FROM NLS_DATABASE_PARAMETERS |
        | Log Many | ${rowCount} |
        """
        cursor = None
        try:
            cursor = self.connection.cursor()
            self.__execute_sql(cursor, selectStatement)
            cursor.fetchall()
            return cursor.rowcount
        finally:
            if cursor:
                self.connection.rollback()

    def execute_sql_string(self, sqlString):
        """
        Executes the sqlString as SQL commands.\n
        Example usage:
        | Execute Sql String | SELECT * FROM NLS_DATABASE_PARAMETERS |
        """
        try:
            cursor = self.connection.cursor()
            self.__execute_sql(cursor, sqlString)
            self.connection.commit()
        finally:
            if cursor:
                self.connection.rollback()

    def execute_sql_script(self, sqlScriptFileName):
        """
        Executes the content of the `sqlScriptFileName` as SQL commands.
        Useful for setting the database to a known state before running
        your tests, or clearing out your test data after running each a
        test.\n
        Example usage:
        | Execute Sql Script | setup.sql |
        # do some stuff here
        | Execute Sql Script | teardown.sql |
        This method provide execution PL/SQL script files.\n
        For example:\n
        DECLARE\n
	        SAUSR_USER_ID$1 PLS_INTEGER;\n

        BEGIN\n

	        EXECUTE IMMEDIATE 'alter session set NLS_TIMESTAMP_TZ_FORMAT = ''YYYY-MM-DD HH24:MI:SS.FF TZH:TZM''';\n

	        INSERT\n
	        INTO SA_USER ("SAUSR_NAME", "SAUSR_MIDDLE_NAME", "SAUSR_LAST_NAME", "SAUSR_LOGIN", "SAUSR_PASSWORD")\n
	        VALUES ('Vasiliy', 'Sergeevich', 'Zaycev', 'vzaycev', '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5');\n

	        SELECT max(SAUSR_USER_ID)\n
	        INTO SAUSR_USER_ID$1\n
	        FROM SA_USER;\n

	        INSERT\n
	        INTO SA_ROLE_USER ("SAUSR_USER_ID", "SARLE_ROLE_ID")\n
	        VALUES (SAUSR_USER_ID$1, 1);\n

        END;
        """
        try:
            cursor = self.connection.cursor()
            self.__execute_sql(cursor, open(sqlScriptFileName, "r").read())
            self.connection.commit()
        finally:
            if cursor:
                self.connection.rollback()

    def __execute_sql(self, cursor, sqlStatement):
        logger.debug("Executing : %s" % sqlStatement)
        cursor.prepare(sqlStatement)
        return cursor.execute(None)