from RandomConnectionSolution import Student
import numpy as np
from tabulate import tabulate
from dbInfo import cursor

def mbti_score(mbti_one, mbti_two):
    sql = f"SELECT * FROM mbti_score WHERE mbti_one = '{mbti_one}' and mbti_two = '{mbti_two}';"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result : return result["mu_score"]
    else : return 0

def interest_score(student_1_id , student_2_id):
    sql = f""" 
    SELECT interest_id 
    FROM student_interest
    WHERE student_id LIKE '{student_1_id}' AND interest_id IN (
    SELECT interest_id
    FROM student_interest
    WHERE student_id LIKE '{student_2_id}');
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    return len(result) 

def two_student_score(student_1, student_2):
    result = mbti_score(student_1["MBTI"] , student_2["MBTI"])
    result += interest_score(student_1["student_id"], student_2["student_id"])
    result -= abs(student_1["birth"].year - student_2["birth"].year)
    if(student_1["place"] == student_2["place"]) : result += 1
    return result
     
def score_algorithm(set_of_student_id):
    stu_list = Student.set_student_info(set_of_student_id)
    matrix = np.zeros([len(stu_list), len(stu_list)])
    for i in range(len(stu_list)):
        for j in range(len(stu_list)):
            if i == j : continue        
            matrix[i][j] = two_student_score(stu_list[i] , stu_list[j])
    return matrix

if  __name__ == "__main__":
    print(score_algorithm({'11112222','11113333'}))



