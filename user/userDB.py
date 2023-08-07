from database.db import databaseHandler

class UserDb:
    def add_user(self, user):
        """
        this method add a record to users table in database
        :param user:
        :return : boolean value
        """
        try:
            sql = "INSERT INTO users (user_name) VALUES (?);"
            database_handler = databaseHandler.DatabaseHandler()
            con = database_handler.get_connection()
            params = (user.user_name,)
            cursor = database_handler.get_cursor(con)
            cursor.execute(sql, params)
            con.commit()
            database_handler.close_connection(con)
            return True

        except Exception as err:
            print(err)
            return False


    def update_user(self, user):
        """
        this method updates the username in database
        :param user:
        :return: boolean
        """
        try:
            sql = "UPDATE users SET user_name = ? WHERE user_id = ?"
            database_handler = databaseHandler.DatabaseHandler()
            con = database_handler.get_connection()
            cursor = database_handler.get_cursor(con)
            cursor.execute(sql,(user.user_name, user.user_id))
            con.commit()
            database_handler.close_connection(con)
            return True
        except Exception as err:
            print(err)
            return False

    def get_all_users(self):
        try:
            sql = "SELECT * FROM users"
            database_handler = databaseHandler.DatabaseHandler()
            con = database_handler.get_connection()
            cursor = database_handler.get_cursor(con)
            cursor.execute(sql)
            users_list = cursor.fetchall()
            return users_list
        except Exception as err:
            print(err)