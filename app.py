from db import databaseHandler
from user.user import User
from user.userDB import UserDb
from skills.skillDB import SkillDB
from skills.skill import Skill

# getting a choice from the user
choice = input("Please Select Your Choice :\n"
               "a: add user\n" #
               "A: add skill\n" #
               "u: update skill\n"#
               "U: update user\n" #
               "d: delete skill\n"#
               "s: show all users\n"
               "S: show user skills\n" #
               "q: quit\n")

# create the database tables
database_handler = databaseHandler.DatabaseHandler()
con = database_handler.get_connection()
database_handler.create_db_tables()

# adding user
if choice == "a":
    # user_id = input("Please enter the user id:\n")
    user_name = input("Please enter the user name:\n")
    user = User(user_name)
    user_db = UserDb()
    is_added = user_db.add_user(user)
    if is_added == True:
        print(f"user {user.user_name} added successfuly")
    else:
        print("can't add this user")

elif choice == "U":
    user_id = input("Please enter the user's ID:\n")
    new_user_name = input("Please enter the new username:\n")
    user = User(new_user_name)
    user.user_id = user_id
    user_db = UserDb()
    is_updated = user_db.update_user(user)
    if is_updated == True:
        print("user updated successfuly")
    else:
        print("can't update this user")

# showing all users
elif choice == "s":
    user_db = UserDb()
    users_list = user_db.get_all_users()
    print(dict(users_list))
    print("users List =>")
    print("#"*50)
    for record in users_list:
        print(record[0], end=": ")
        print(record[1])

# adding a new skill to user
elif choice == "A":
    skill_db = SkillDB()
    user_id = int(input("Please enter the user ID:\n"))
    user_db = UserDb()
    users_list = user_db.get_all_users()
    user_dict = dict(users_list)
    user_name = user_dict[user_id]
    skill_name = input("Please enter the skill name:\n").capitalize()
    skill_progress = input("Please enter the skill progress:\n")
    skill = Skill(user_id,skill_name,skill_progress+"%")
    is_added = skill_db.add_skill(skill)
    if is_added == True:
        print("skill added successfuly")
    else:
        print("can't add this skill")

# update skill
elif choice == "u":
    user_id = int(input("Please enter user ID:\n"))
    skill_name = input("Please enter the skill name:\n").capitalize()
    new_skill_progress = input("Please enter the new skill progress:\n")

    skill = Skill(user_id , skill_name, new_skill_progress +"%")

    skill_db = SkillDB()

    is_updated = skill_db.update_skill(skill)
    if is_updated == True:
        print("skill updated successfully")
    else :
        print("can't update this skill")

# delete skill
elif choice == "d":
    user_id = int(input("Please enter user ID:\n"))
    skill_name = input("Please enter the skill name:\n").capitalize()
    skill = Skill(user_id, skill_name,None)
    skill_db = SkillDB()
    is_deleted = skill_db.delete_skill(skill)

    if is_deleted == True:
        print("skill deleted successfully")
    else:
        print("can't delete this skill")

elif choice == "S":
    user_id = input("Please enter the user ID:\n")
    skill_db = SkillDB()
    skill_db.show_skills(user_id)

else:
    print("#" * 50)