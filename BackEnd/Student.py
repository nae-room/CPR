import pandas as pd
import time
import pymysql
from dbInfo import cursor
from tabulate import tabulate

student_matched = dict()

def print_tab(students):
    print(tabulate(students, headers = 'keys'))

def stu_parsing(set_of_student_id):
    string = "("
    for x in set_of_student_id:
        string += "'" + x + "',"
    string = string[0: len(string) - 1]
    string += ')'
    return string

def student_info(student_id):
    sql = "SELECT * FROM students WHERE student_id = '" + student_id + "';"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result : return result
    else : return False

def all_student_info():
    sql = "SELECT * FROM students;"
    cursor.execute(sql)
    result = pd.DataFrame(cursor.fetchall())
    return result

def set_student_info(set_of_student_id):
    string = stu_parsing(set_of_student_id)
    sql = f"SELECT * FROM students WHERE student_id IN {string}"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result    
    
def student_load(student_id, passward):
    sql = "SELECT * FROM students WHERE student_id = '" + student_id + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) == 0 :return False
    elif result[0]['passward'] == passward and result[0]['is_online'] == 0 : 
        sql = "UPDATE students SET is_online = TRUE"
        cursor.execute(sql)
        return True
    else : return False

def is_student_online(student_id):
    sql = "SELECT is_online FROM students WHERE student_id = '" + student_id + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) == 0: return False
    elif result[0]['is_online'] == True :
        return True
    else : return False

def student_deload(student_id):
    sql = "SELECT * FROM students WHERE student_id = '" + student_id + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) == 0 :return False
    elif result[0]['is_online'] == 1 : 
        sql = "UPDATE students SET is_online = FALSE"
        cursor.execute(sql)
        return True
    else : return False

def student_matching(student_1_id, student_2_id):
    sql = "SELECT student_id, is_online FROM students WHERE student_id in (" + student_1_id + " , " + student_2_id + ");"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) < 2 : return False
    elif result[0]["is_online"] == 1 and result[1]["is_online"] == 1 and student_1_id not in student_matched and student_2_id not in student_matched :
        sql = "INSERT INTO conversation(student_1_id, student_2_id, start_time, end_time) VALUE (" + student_1_id + "," + student_2_id + ",'" + time.strftime('%Y-%m-%d %I:%M:%S') + "','" + time.strftime('%Y-%m-%d %I:%M:%S') + "');"
        cursor.execute(sql)
        sql = "SELECT conversation_id FROM conversation ORDER BY conversation_id DESC limit 1;"
        cursor.execute(sql)
        result = cursor.fetchall()
        student_matched[student_1_id] = result[0]["conversation_id"]
        student_matched[student_2_id] = result[0]["conversation_id"]
        return True
    else : return False

def student_dematching(student_1_id, student_2_id):
    if(student_1_id not in student_matched.keys() or student_2_id not in student_matched.keys()) :return False
    number = student_matched[student_1_id]
    sql = "UPDATE conversation SET end_time = '" + time.strftime('%Y-%m-%d %I:%M:%S') + "' WHERE conversation_id = " + str(number) + ";"
    cursor.execute(sql)
    del student_matched[student_1_id]
    del student_matched[student_2_id]
    return True

def all_matching_info():
    for x in student_matched :
        print(x)

def all_conversation_info() :
    sql = "SELECT conversation_id, student_1_id, student_2_id, start_time, end_time FROM conversation;"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(tabulate(pd.DataFrame(result),headers = 'keys'))

def add_friend(from_student , to_student):
    sql = "SELECT * FROM friend WHERE from_student_id = " + from_student + ";"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) < 1 :
        sql = "INSERT INTO friend(from_student_id, to_student_id) VALUE (" + from_student + ", " + to_student + ");"
        cursor.execute(sql)
        return True
    else :
        return False

def del_friend(from_student, to_student):
    sql = "SELECT * FROM friend WHERE from_student_id = " + from_student + " and to_student_id = " + to_student +  ";"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) > 0 :
        sql = "DELETE FROM friend WHERE from_student_id = " + from_student + " and to_student_id = " + to_student +  ";"
        cursor.execute(sql)
        return True
    else :
        return False

def who_is_my_friend(student_id):
    sql = "SELECT * FROM friend WHERE from_student_id = " + student_id + ";"
    cursor.execute(sql)
    print(tabulate( cursor.fetchall(), headers = 'keys'))

def update_score(from_student, to_student, score):
    sql = "SELECT * FROM score WHERE from_student_id = " + from_student + " and to_student_id = " + to_student +  ";"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) > 0 :
        sql = "UPDATE score SET score = " + str(score) + "WHERE from_student_id = " + from_student + " and to_student_id = " + to_student +  ";"
        cursor.execute(sql)
    else :
        sql = "INSERT INTO score(from_student_id, to_student_id, score) VALUE (" + from_student + ", " + to_student + "," + str(score) + ");"
        cursor.execute(sql)

def my_score_to(from_student, to_student):
    sql = "SELECT score FROM score WHERE from_student_id = " + from_student + " and to_student_id = " + to_student +  ";"
    cursor.execute(sql)
    result = cursor.fetchone()
    if(result):
        print(result["score"])
        return True
    else :
        return False

def all_score():
    sql = "SELECT * FROM score;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
  
if __name__ == "__main__":
    all_student_info()
    all_conversation_info()
    all_matching_info()
    all_score()
    