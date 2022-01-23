from RandomConnectionSolution import Student
import numpy as np
from tabulate import tabulate
from dbInfo import cursor
from collections import OrderedDict

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
     
def score_algorithm(list_of_student_id):
    stu_list = Student.list_student_info(list_of_student_id)
    matrix = np.zeros([len(stu_list), len(stu_list)])
    for i in range(len(stu_list)):
        for j in range(len(stu_list)):
            if i == j : continue        
            matrix[i][j] = two_student_score(stu_list[i] , stu_list[j])
    return matrix, list_of_student_id

def greedy_score(matrix_of_score, stu_list):
    matching_dict = dict()
    ordered_dict = OrderedDict()
    visit = {i : False for i in range(len(stu_list))}
    for i in range(len(stu_list)) :
        for j in range( len(stu_list) ): 
            ordered_dict[matrix_of_score[i][j]] = (i, j)
    for i, j in ordered_dict.values() :
        if i == j : pass
        elif visit[i] == True or visit[j] == True : pass
        else : 
            matching_dict[stu_list[i]] = stu_list[j]
            visit[i] = True
            visit[j] = True
    return matching_dict

if  __name__ == "__main__":
   print(greedy_score(*score_algorithm(['11112222','11113333'])))