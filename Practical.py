#Create the below series using dictionary
#  A  10
#  B  20
#  C  30
#  D  40
#  E  50 

import pandas as pd
S = pd.Series({'A' : '10', 'B' : '20', 'C' : '30', 'D' : '40', 'E' : '50'})
#print(S)

# Q2) Create the below series and give name to index
#  Month    
#   JAN    31
#   FEB    28
#   MAR    31
#   APR    30
#   MAY    31

import pandas as pd
data = {'JAN': 31, 'FEB': 28, 'MAR': 31, 'APR': 30, 'MAY': 31}
my_series = pd.Series(data)
my_series.index.name = 'Month'
#print(my_series)

# Q3) Create the below series and perform all mathematical operations 
#   s1                  s2
# 1    2            101    3
# 2    4            102    5
# 3    6            103    7
# 4    8             1     9
# 5   10             2    11
# 6   12             5    13

import pandas as pd

data_s1 = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12}
s1 = pd.Series(data_s1, name='S1')

data_s2 = {1: 3, 2: 5, 3: 7, 4: 9, 5: 11, 6: 13}
s2 = pd.Series(data_s2, name='S2')

addition_result = s1 + s2

subtraction_result = s1 - s2

multiplication_result = s1 * s2

division_result = s1 / s2

#print("\nAddition Result:")
#print(addition_result)

#print("\nSubtraction Result:")
#print(subtraction_result)

#print("\nMultiplication Result:")
#print(multiplication_result)

#print("\nDivision Result:")
#print(division_result)


# Q4) Create the series that stores salaries of 7 employee and then write code to print 
# 1) Total no. of employee
# 2) Check whether series is empty
# 3) Check whether series has NaN values
# 4) Count not NaN values in series
# 5) Print only name of employee

import pandas as pd
import numpy as np

salaries = pd.Series([50000, 60000, 75000, 55000, 70000, np.nan, 80000], name='Salaries')

total_employees = len(salaries)

is_empty = salaries.empty

has_nan = salaries.isnull().any()

non_nan_count = salaries.count()

employee_names = ["Employee 1", "Employee 2", "Employee 3", "Employee 4", "Employee 5", "Employee 6", "Employee 7"]

#print("1) Total number of employees:", total_employees)
#print("2) Is the Series empty?", is_empty)
#print("3) Does the Series have NaN values?", has_nan)
#print("4) Count of non-NaN values in the Series:", non_nan_count)
#print("5) Names of employees:")
#for i in range(len(employee_names)):
    #print(f"{employee_names[i]}")

# Q5) Create a series temp that stores temperature of 7 days. Its index should be Sunday, Monday, Tuesday, Wednesday....... also write code for -
# 1) Display temperature of first 3 days 
# 2) Display temperature of last 4 days
# 3) Display temperature in reverse order
# 4) Display temperature from tuesday to friday

import pandas as pd

temp_data = {'Sunday': 30, 'Monday': 28, 'Tuesday': 32, 'Wednesday': 29, 'Thursday': 31, 'Friday': 27, 'Saturday': 33}
temp = pd.Series(temp_data, name='Temperature')

first_3_days = temp[:3]

last_4_days = temp[-4:]

temp_reverse = temp[::-1]

tuesday_to_friday = temp['Tuesday':'Friday']

#print("1) Temperature of the first 3 days:")
#print(first_3_days)

#print("\n2) Temperature of the last 4 days:")
#print(last_4_days)

#print("\n3) Temperature in reverse order:")
#print(temp_reverse)

#print("\n4) Temperature from Tuesday to Friday:")
#print(tuesday_to_friday)


# Q6) Create an empty dataframe named as empty dataframe

import pandas as pd

empty_dataframe = pd.DataFrame()

#print(empty_dataframe)

# Q7) Create a dataframe named as students using a list of names of 5 students 

import pandas as pd

student_names = ['Jatin', 'Srijan', 'Ada', 'Maithily', 'Kanishka']

students = pd.DataFrame({'Student Name': student_names})

#print(students)


# Q8) Create a dataframe players using a list of names and scores of the previous three matches 

import pandas as pd

player_names = ['Player1', 'Player2', 'Player3', 'Player4', 'Player5']

match_scores = [
    [80, 75, 90],
    [65, 70, 85],
    [95, 88, 92],
    [72, 68, 78],
    [88, 82, 91]
]

players = pd.DataFrame({
    'Player Name': player_names,
    'Match 1 Score': [scores[0] for scores in match_scores],
    'Match 2 Score': [scores[1] for scores in match_scores],
    'Match 3 Score': [scores[2] for scores in match_scores]
})

#print(players)















