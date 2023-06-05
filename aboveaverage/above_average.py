"""
How to get input from file to run program.
type input.txt | python .\above_average.py
"""

def calculate_avg(grades):
    sum = 0
    for i in grades:
        sum += i
    return sum / N

def amount_above_avg(grades, avg):
    above_avg = 0

    for grade in grades:
        if grade > avg:
            above_avg += 1

    return above_avg

def convert_to_percentile(N, res):
    return res / N * 100

''' Problem solution '''
C = int(input()) # number of test cases

for i in range(C):
    data_sets = input().split() # all inputs
    N = int(data_sets[0]) # number of people in the class
    student_grades = [int(num) for num in data_sets[1:]] # all the student grades, of size N

    avg = calculate_avg(student_grades)
    res = amount_above_avg(student_grades, avg)
    answer = convert_to_percentile(N, res)
    answer = "%.3f" % answer
    print(f"{answer}%")