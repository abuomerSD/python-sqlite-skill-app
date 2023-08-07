from database.db.databaseHandler import DatabaseHandler

class SkillDB:
    """
    this method add a new skills record to the skill table on database
    :return: boolean
    :param: skill object
    """
    def add_skill(self, skill):

        try:
            sql = "INSERT INTO skills VALUES (?,?,?)"
            user_id = skill.user_id
            skill_name = skill.skill_name
            skill_progress = skill.skill_progress
            database_handler = DatabaseHandler()
            con = database_handler.get_connection()
            cursor = database_handler.get_cursor(con)
            cursor.execute(sql, (user_id, skill_name, skill_progress))
            con.commit()
            database_handler.close_connection(con)
            return True

        except Exception as err:
            print(err)
            return False

    """
    this method updates the skill progress on database
    :return:boolean
    :param: skill objects
    """
    def update_skill(self, skill):
        try:
            sql = "UPDATE skills SET skill_progress = ? WHERE user_id = ? and skill_name = ?"
            skill_progress = skill.skill_progress
            user_id = skill.user_id
            skill_name = skill.skill_name
            database_handler = DatabaseHandler()
            con = database_handler.get_connection()
            cursor = database_handler.get_cursor(con)
            cursor.execute(sql,(skill_progress, user_id, skill_name))
            con.commit()
            database_handler.close_connection(con)
            return True

        except Exception as err:
            print(err)
            return False

    def delete_skill(self, skill):
        """
        this method delete a skill
        :return: boolean
        """
        try:
            sql = "DELETE FROM skills where user_id = ? and skill_name = ?"
            database_handler = DatabaseHandler()
            con = database_handler.get_connection()
            cursor = database_handler.get_cursor(con)
            print(f"{skill.user_id} {skill.skill_name}")
            cursor.execute(sql,(skill.user_id, skill.skill_name))
            con.commit()
            return True
        except Exception as err:
            print(err)
            return False

    def show_skills(self,user_id):
        """
        this method print all user skills
        :param user_id:
        :return:
        """
        try:
            skill_sql = "SELECT * FROM skills where user_id = ?"
            database_handler = DatabaseHandler()
            con = database_handler.get_connection()
            cursor = database_handler.get_cursor(con)
            cursor.execute(skill_sql, (user_id,))
            skills_list = cursor.fetchall()
            # print(skills_list)
            for record in skills_list:
                print(record[1], end=": ")
                print(record[2])
        except Exception as err:
            print(err)