# -*- encoding: utf-8 -*-
# Copyright (c) 2013 Roman Merkushin
# rmerkushin@ya.ru

class Assertion(object):
    """
    Assertion handles all the assertions of Database Library.
    """

    def query_result_should_contain(self, selectStatement, content):
        """
        Check if query result returned from `selectStatement` is equal to the content submitted.
        If query result and defined content is not equal, then this will throw an AssertionError.
        Content values should be written with semicolon delimited.\n
        Example usage:
        | Query Result Should Contain | SELECT USER_NAME FROM USERS WHERE ROLE_ID = 1 | John;Adam;Jack;Maria; |
        """
        result = ""
        queryResult = self.query(selectStatement)
        for row in queryResult:
            for value in row:
                result += str(value) + ";"
        if result != content:
            raise AssertionError("Expected to have query result equal to '%s' "
                                 "but it is : '%s'." % (content, result))

    def check_if_exists_in_database(self, selectStatement):
        """
        Check if any row would be returned by given the input `selectStatement`.
        If there are no results, then this will throw an AssertionError.\n
        Example usage:
        | Check If Exists In Database | SELECT USER_NAME FROM USER WHERE WHERE USER_NAME = 'Jack' |
        """
        if not self.query(selectStatement):
            raise AssertionError("Expected to have at least one row from '%s' "
                                 "but got 0 rows." % selectStatement)

    def check_if_not_exists_in_databese(self, selectStatement):
        """
        This is the negation of `check_if_exists_in_database`.
        Check if no rows would be returned by given the input `selectStatement`.
        If there are any results, then this will throw an AssertionError.\n
        Example usage:
        | Check If Exists In Database | SELECT USER_NAME FROM USER WHERE WHERE USER_NAME = 'Jack' |
        """
        queryResults = self.query(selectStatement)
        if queryResults:
            raise AssertionError("Expected to have have no rows from '%s' "
                                 "but got some rows : %s." % (selectStatement, queryResults))

    def row_count_is_equal_to_x(self, selectStatement, numRows):
        """
        Check if the number of rows returned from `selectStatement` is equal to the value submitted.
        If not, then this will throw an AssertionError.
        """
        num_rows = self.row_count(selectStatement)
        if num_rows != int(numRows):
            raise AssertionError("Expected same number of rows to be returned from '%s' "
                                 "than the returned rows of %s" % (selectStatement, num_rows))