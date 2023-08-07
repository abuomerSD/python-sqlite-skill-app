import sqlite3

class DatabaseHandler:
    """
    this class is to return database connection and cursor for all the app .
    """
    __database_path = "E:\python\learning python\database\\"
    __con = None

    def get_connection(self):
        """
        :return:connection object
        """
        try:
            __con = sqlite3.connect(self.__database_path + "database.db")
            print("Connection Established")
            return __con

        except:
            print("Connection Error")

    def close_connection(self, connection):
        """
        :param connection: it takes the connection which you want to close and it will close it .
        :return:
        """

        if connection != None:
            connection.close()
            print("Connection Closed")
        else:
            print("no connection found")

    def get_cursor(self, connection):
        """
        :param connection: the connection you just established
        :return: cursor object
        """

        if connection != None:
            cursor = connection.cursor()
            print("cursor returned")
            return cursor
        else:
            print("You Must Have Connection First")

    def create_db_tables(self):
        tb1_sql = "CREATE TABLE IF NOT EXISTS users(" \
                  "user_id INTEGER," \
                  "user_name TEXT," \
                  "PRIMARY KEY('user_id' AUTOINCREMENT));"

        tb2_sql = "CREATE TABLE IF NOT EXISTS skills(" \
                  "user_id INTEGER," \
                  "skill_name TEXT," \
                  "skill_progress TEXT);"


        try:
            con = self.get_connection()
            cursor = self.get_cursor(con)
            cursor.execute(tb1_sql)
            cursor.execute(tb2_sql)
            self.close_connection(con)
        except Exception as err:
            print(err)
            self.close_connection(con)




